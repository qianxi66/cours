# ，包含数据库的连接、初始化和基本的CRUD操作


import sqlite3  
# model/database.py  
from sqlalchemy import create_engine  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker 
# db.py  
from model.database import engine  
from model import models   

engine = create_engine('sqlite:///database.db', echo=False)  
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)  
Base = declarative_base()




def init_db():  
    models.Base.metadata.create_all(bind=engine)  

if __name__ == '__main__':  
    init_db()  
    print('数据库初始化完成！')