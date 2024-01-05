from model.da.database import DataBaseManager, and_, or_, between
from model.entity import *


class SupplierProducerProductDa(DataBaseManager):
    def find_by_producer_and_omniclasscode(self, omniclass_code,producer_id):
        self.make_engine()
        result = self.session.query(ProducerProductClass).filter(
            and_(ProducerProductClass.producer_id == producer_id, ProducerProductClass.omniclass_code == omniclass_code)).all()
        for row in result:
            if self.session.query(SupplierProducerProduct).filter(SupplierProducerProduct.id == row.id):
                x = self.session.query(SupplierProducerProduct).filter(SupplierProducerProduct.id == row.id)
        self.session.close()
        return x

