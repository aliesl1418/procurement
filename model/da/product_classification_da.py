from model.da.database import DataBaseManager, and_, or_, between
from model.entity import *


class ProductClassificationDa(DataBaseManager):
    def find_by_omniclasscode(self, omniclass_code):
        self.make_engine()
        result = self.session.query(ProductClassification).filter(
            ProductClassification.omniclass_code == omniclass_code).all()
        if result:
            return result[0]

    def find_by_omniclassname(self, omniclass_name):
        self.make_engine()
        result = self.session.query(ProductClassification).filter(
            ProductClassification.omniclass_name == omniclass_name).all()
        if result:
            return result[0]

    def find_by_omniclasslevel(self, omniclass_level):
        self.make_engine()
        result = self.session.query(ProductClassification).filter(
            ProductClassification.omniclass_level == omniclass_level).all()
        if result:
            return result


