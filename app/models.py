from sqlalchemy import Column, Integer, String
from hackjam2014.database import Base

class User(Base):
    __tablename__='user'
    id=Column(integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(120), unique=True)
    
    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email
    
     def is_active(self):
         return True
    
     def get_id(self):
         return self.email
    
     def is_authenticated(self):
         return self.authenticated
    
     def is_anonymous(self):
         return False