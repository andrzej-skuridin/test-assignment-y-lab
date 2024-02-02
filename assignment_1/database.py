from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import PostgresDsn

#PostgreSQL:
SQLALCHEMY_DATABASE_URL = "postgresql+psycopg2://core:wCh29&HE&T83@localhost/y_lab_assignment_1_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
