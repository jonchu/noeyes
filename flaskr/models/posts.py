from sqlalchemy import (TIMESTAMP, Column, ForeignKey, Integer, String, Text,
                        create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class Post(Base):
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    created = Column(TIMESTAMP, nullable=False, server_default=func.now())
    title = Column(Text, nullable=False)
    body = Column(Text, nullable=False)
    
    def __init__(self, author_id, title, body):
        self.author_id = author_id
        self.title = title
        self.body = body

    def __repr__(self):
        return "Post(author_id=%r, created=%r, title=%r, body=%r)" % (
            self.author_id,
            self.created,
            self.title,
            self.body
        )