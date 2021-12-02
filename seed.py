from models import engine, db_session, Base, User, Todo

Base.metadata.create_all(bind=engine)

test1 = User(username="test1")
db_session.add(test1)
test2 = User(username="test2")
db_session.add(test1)

todo1 = Todo(content="Todo Content 1", important=True, user=test1)
db_session.add(todo1)
todo2 = Todo(content="Todo Content 2", important=False, user=test1)
db_session.add(todo2)
todo3 = Todo(content="Todo Content 3", important=False, user=test2)
db_session.add(todo3)
todo4 = Todo(content="Todo Content 4", important=True, user=test2)
db_session.add(todo4)

db_session.commit()
