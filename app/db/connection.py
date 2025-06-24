import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# rode no terminal uvicorn app.main:app --reload
def init_db():
    import model.models  # Import models to ensure they are registered with SQLAlchemy
    Base.metadata.create_all(bind=engine)
    print("Banco de dados inicializado com sucesso!")
    