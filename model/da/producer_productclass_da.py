from model.da.database import DataBaseManager, and_, or_, between
from model.entity import *


class ProducerProductClassDa(DataBaseManager):
    def find_by_omniclasscode(self, omniclass_code):
        self.make_engine()
        result = self.session.query(ProducerProductClass).filter(
            ProducerProductClass.omniclass_code == omniclass_code).all()
        for row in result:
            if self.session.query(Producer).filter(Producer.id == row.producer_id):
                x = self.session.query(Producer).filter(Producer.id == row.producer_id)
        self.session.close()
        return x

    def find_by_producer_id(self, producer_id):
        self.make_engine()
        result = self.session.query(ProducerProductClass).filter(
            ProducerProductClass.producer_id == producer_id).all()
        for row in result:
            if self.session.query(ProductClassification).filter(ProductClassification.omniclass_code == row.omniclass_code):
                x = self.session.query(ProductClassification).filter(ProductClassification.omniclass_code == row.omniclass_code)
        self.session.close()
        return x


