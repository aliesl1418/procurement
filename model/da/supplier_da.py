from model.da.database import DataBaseManager,and_,or_,between
from model.entity import *


class SupplierDa(DataBaseManager):
    def find_by_username_password(self, username, password):
        self.make_engine()
        result = self.session.query(Supplier).filter(
            and_(Supplier.username == username, Supplier.password == password)).all()
        if result:
            return result[0]

    def find_by_username(self, username):
        self.make_engine()
        result = self.session.query(Supplier).filter(Supplier.username == username).all()
        if result:
            return result[0]
