from sqlalchemy.orm import Session
from . import models, schemas

def list_comments(db: Session, post_id: int, skip: int = 0, limit: int = 10):
    return db.query(models.Comment).filter(models.Comment.post_id == post_id).offset(skip).limit(limit).all()

def create_comment(db: Session, comment: schemas.CommentCreate):
    db_comment = models.Comment(**comment.dict())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def update_comment(db: Session, comment_id: int, payload: schemas.CommentUpdate):
    db_comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    if not db_comment:
        return None
    for key, value in payload.dict(exclude_unset=True).items():
        setattr(db_comment, key, value)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def delete_comment(db: Session, comment_id: int):
    db_comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    if not db_comment:
        return None
    db.delete(db_comment)
    db.commit()
    return True
