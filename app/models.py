from sqlalchemy import Column, Integer, String, Enum, DateTime, func
from .db import Base
import enum

# The models.py you shared defines Pydantic models,these models are not database tables—they describe the shape of data for API requests and responses.
class CommentStatus(str, enum.Enum):
    visible = "visible"
    hidden = "hidden"
    deleted = "deleted"

class Comment(Base):
    __tablename__ = "Comment_table"

    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, index=True, nullable=False)
    user_id = Column(String(50), nullable=False)
    content = Column(String(5000), nullable=False)
    status = Column(Enum(CommentStatus), default=CommentStatus.visible)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
