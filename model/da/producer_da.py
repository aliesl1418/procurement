from model.da.database import DataBaseManager,and_,or_,between
from model.entity import *


class ProducerDa(DataBaseManager):
    def find_by_username_password(self, username, password):
        self.make_engine()
        result = self.session.query(Producer).filter(
            and_(Producer.username == username, Producer.password == password)).all()
        if result:
            return result[0]

    def find_by_username(self, username):
        self.make_engine()
        result = self.session.query(Producer).filter(Producer.username == username).all()
        if result:
            return result[0]
