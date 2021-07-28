from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from .base import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String, default=None)
    status = Column(String, default='user')
    language = Column(String, default='en')
    created_at = Column(DateTime, default=datetime.utcnow)

    def is_admin(self) -> bool:
        return self.status in ['admin', 'super_admin']

    def is_super_admin(self) -> bool:
        return self.status == 'super_admin'

    def __repr__(self) -> str:
        return f'<User {self.username}>'
