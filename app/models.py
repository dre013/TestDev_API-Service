from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Sequence


from app.database import Base


class Quiz(Base):
    __tablename__ = "Quiz"

    number = Column(Integer, Sequence("Id"), primary_key=True, index=True)
    id = Column(Integer, unique=True, index=True)
    question = Column(String, index=True)
    answer = Column(String, index=True)
    creation_date = Column(String, index=True)

