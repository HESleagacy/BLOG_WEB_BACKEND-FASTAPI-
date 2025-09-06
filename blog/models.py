from sqlalchemy import coloumn, Integer, String
from .database import Base


class Blog(Base):
    __tablename__ = 'blogs'
    id = coloumn(Integer, primary_key=True, index = True)
    title = coloumn(String)
    body = coloumn(String)
