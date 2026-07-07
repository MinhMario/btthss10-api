from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

DATABASE_URL = "mysql+pymysql://root:Minh01052007.@localhost/Troll"

engine=create_engine(DATABASE_URL)

LocalSession=sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base=declarative_base()