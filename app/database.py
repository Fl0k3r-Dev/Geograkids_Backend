from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://geousr:P%40ssuord1@localhost:3306/mestrado"
# DATABASE_URL = "mysql+pymysql://mestradoer:Ecidir88#@mestradoer.mysql.dbaas.com.br/mestradoER"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
