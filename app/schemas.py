from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from enum import Enum

class CommentStatus(str, Enum):
    visible = "visible"
    hidden = "hidden"
    deleted = "deleted"

class CommentBase(BaseModel):
    post_id: int
    user_id: str
    content: str
    status: Optional[CommentStatus] = CommentStatus.visible

class CommentCreate(CommentBase):
    pass

class CommentUpdate(BaseModel):
    content: Optional[str] = None
    status: Optional[CommentStatus] = None

class CommentOut(CommentBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
