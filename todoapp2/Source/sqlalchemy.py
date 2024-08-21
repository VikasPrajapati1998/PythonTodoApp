from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Define the SQLAlchemy base class
Base = declarative_base()

# Define the ToDoItem model
class ToDoItem(Base):
    __tablename__ = 'todos'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)

# Create an SQLite database and engine
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, echo=True)

# Create the database table
Base.metadata.create_all(bind=engine)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_todo_item(db: Session, title: str, description: str = None, completed: bool = False):
    db_todo = ToDoItem(title=title, description=description, completed=completed)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def get_todo_item(db: Session, todo_id: int):
    return db.query(ToDoItem).filter(ToDoItem.id == todo_id).first()

def get_all_todo_items(db: Session):
    return db.query(ToDoItem).all()

if __name__ == "__main__":
    # Create a new session
    with SessionLocal() as session:
        # Add a new ToDo item
        new_item = create_todo_item(session, title="Learn SQLAlchemy", description="Study SQLAlchemy ORM", completed=False)
        print(f"Added ToDo item: {new_item}")

        # Retrieve a specific ToDo item by ID
        todo_item = get_todo_item(session, 1)
        print(f"Retrieved ToDo item: {todo_item}")

        # Retrieve all ToDo items
        all_todo_items = get_all_todo_items(session)
        print("All ToDo items:")
        for item in all_todo_items:
            print(item)
