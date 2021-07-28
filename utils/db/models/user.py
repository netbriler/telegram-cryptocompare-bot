from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from .base import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String, default=None)
    language = Column(String, default='en')

    def __repr__(self) -> str:
        return f'<User {self.username}>'
