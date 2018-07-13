import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from createtable import * #changed to createtable as this is the name of my python create table script **yeaz**
 
engine = create_engine('postgresql://postgres:postgres@10.0.0.1:5432/test', echo=True)
 
# create a Session
Session = sessionmaker(bind=engine)
session = Session()
 
user = User("admin","password")
session.add(user)
 
# commit the record the database
session.commit()
 
session.commit()
