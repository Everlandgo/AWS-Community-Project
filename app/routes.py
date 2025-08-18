from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, schemas, db

router = APIRouter()

@router.get("/comments", response_model=list[schemas.CommentOut])
def get_comments(post_id: int, skip: int = 0, limit: int = 10, db_sess: Session = Depends(db.get_db)):
    return crud.list_comments(db_sess, post_id, skip, limit)

@router.post("/comments", response_model=schemas.CommentOut)
def create_comment(payload: schemas.CommentCreate, db_sess: Session = Depends(db.get_db)):
    return crud.create_comment(db_sess, payload)

@router.patch("/comments/{comment_id}", response_model=schemas.CommentOut)
def update_comment(comment_id: int, payload: schemas.CommentUpdate, db_sess: Session = Depends(db.get_db)):
    result = crud.update_comment(db_sess, comment_id, payload)
    if not result:
        raise HTTPException(status_code=404, detail="Comment not found")
    return result

@router.delete("/comments/{comment_id}")
def delete_comment(comment_id: int, db_sess: Session = Depends(db.get_db)):
    result = crud.delete_comment(db_sess, comment_id)
    if not result:
        raise HTTPException(status_code=404, detail="Comment not found")
    return {"message": "Deleted"}
