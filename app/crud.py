from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder


from app import models
from app import schemas


def get_quiz_by_id(db: Session, quiz_id: int):
    return db.query(models.Quiz).filter(models.Quiz.id == quiz_id).first()



def get_quizzes(db: Session):
    return db.query(models.Quiz).all()


def create_quiz(db: Session, quiz: schemas.Qiuz):
    db_quiz = models.Quiz(id=quiz.id, question=quiz.question, answer=quiz.answer, creation_date=quiz.creation_date)
    db.add(db_quiz)
    db.commit()
    db.refresh(db_quiz)
    return db_quiz


def get_last_quiz(db: Session):
    try:
        return db.query(models.Quiz).all()[-2]
    except:
        return schemas.Qiuz(id = 0, question = "string", answer = "string", creation_date = "string")



def put_quiz(db: Session, quiz_id: int, quiz: schemas.Qiuz):
    db_quiz_post = db.query(models.Quiz).filter(models.Quiz.id == quiz_id).first()
    if db_quiz_post is None:
        return db_quiz_post
    db_quiz_post.number = db_quiz_post.number
    db_quiz_post.id = quiz.id
    db_quiz_post.question = quiz.question
    db_quiz_post.answer = quiz.answer
    db_quiz_post.creation_date = quiz.creation_date
    db.commit()
    return db_quiz_post


def delete_quiz(db: Session, quiz_id: int) -> bool:
    db_quiz = bool(db.query(models.Quiz).filter(models.Quiz.id == quiz_id).delete())
    db.commit()
    return db_quiz


def delete_all(db: Session):
    database = db.query(models.Quiz).all()
    if len(database) > 0:
        for i in range(len(database)):
            db_quiz = bool(db.query(models.Quiz).filter(models.Quiz.id == database[i].id).delete())
        db.commit()
        return db_quiz 
    else:
        return False



