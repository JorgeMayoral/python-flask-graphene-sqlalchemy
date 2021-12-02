import uuid

from sqlalchemy import *
from sqlalchemy.orm import scoped_session, sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///database.sqlite3', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class User(Base):
    __tablename__ = "user"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    username = Column(String)


class Todo(Base):
    __tablename__ = "todo"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    content = Column(String)
    important = Column(Boolean)
    created_at = Column(DateTime, default=func.now())
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User, backref=backref('todos', uselist=True, cascade="delete,all"))
