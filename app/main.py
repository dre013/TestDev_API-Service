from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session


from app import crud
from app import models
from app import schemas
from app import request
from app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/quizzes/{questions_num}", response_model=schemas.Qiuz)
async def create_quiz(questions_num: int, db: Session = Depends(get_db)):
    resp = request.request_function(questions_num)
    quiz = schemas.Qiuz
    for question in resp:
        quiz_response = quiz(id = question['id'], question = question['question'], answer = question['answer'], creation_date = question['created_at'])
        db_quiz = crud.create_quiz(db, quiz=quiz_response)
        if db_quiz:
            next
        else:
            crud.create_quiz(db, quiz=quiz_response)
    return crud.get_last_quiz(db)


@app.get("/quizzes/", response_model=list[schemas.Qiuz])
async def get_quizzes(db: Session = Depends(get_db)):
    quizzes = crud.get_quizzes(db)
    return quizzes


@app.get("/quizzes/{quiz_id}", response_model=schemas.Qiuz)
async def get_quiz(quiz_id: int, db: Session = Depends(get_db)):
    db_quiz = crud.get_quiz_by_id(db, quiz_id=quiz_id)
    if db_quiz is None:
        raise HTTPException(status_code=404, detail="Quiz not found")
    return db_quiz


@app.put("/quizzes/{quiz_id}", response_model=schemas.Qiuz)
async def put_quiz(quiz_id: int, quiz: schemas.Qiuz, db: Session = Depends(get_db)):
    db_put = crud.put_quiz(quiz_id=quiz_id, quiz=quiz, db=db)
    if db_put is None:
        raise HTTPException(status_code=404, detail="Quiz not found")
    try:
        return db_put
    except:
        return {"Error":"Your request is incorrect, please enter request in dictionary format"}


@app.delete("/quizzes/delete/{quiz_id}")
async def delete_quiz(quiz_id: int, db: Session = Depends(get_db)):
    db_quiz = crud.delete_quiz(db, quiz_id=quiz_id)
    if db_quiz is False:
        raise HTTPException(status_code=404, detail="Quiz not found")   
    return {f'id {quiz_id} status': 'deleted'}


@app.delete("/quizzes/delete/all/")
async def delete_all(db: Session = Depends(get_db)):
    db_quiz = crud.delete_all(db)
    if db_quiz is False:
        raise HTTPException(status_code=404, detail="Database is empty")   
    return {"Database deletion status": f"{db_quiz}"}

