import json
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    def to_json(self):
        return str({c.name: str(getattr(self, c.name)) for c in self.__table__.columns})


    def __repr__(self):
        return str({c.name: str(getattr(self, c.name)) for c in self.__table__.columns})
