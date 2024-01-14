from model.da.database import DataBaseManager, and_, or_, between
from model.entity import *


class SupplierProducerProductDa(DataBaseManager):
    def find_by_supplier_and_producer_productclass(self, supplier_id, producerproductclass_id):
        self.make_engine()
        result = self.session.query(SupplierProducerProduct).filter(
            and_(SupplierProducerProduct.supplier_id == supplier_id,
                 SupplierProducerProduct.producerproductclass_id == producerproductclass_id)).all()
        self.session.close()
        return result

    def find_by_supplier_id(self, supplier_id):
        self.make_engine()
        result = self.session.query(SupplierProducerProduct).filter(
            SupplierProducerProduct.supplier_id == supplier_id).all()
        self.session.close()
        return result

    def find_by_producer_name_and_omniclass_code(self, producer_name, omniclass_code, supplier_id):
        self.make_engine()
        result = self.session.query(SupplierProducerProduct).join(SupplierProducerProduct.producerproductclass_r). \
            join(ProducerProductClass.producer_r). \
            filter(and_(Producer.name == producer_name, ProducerProductClass.omniclass_code == omniclass_code,
                        SupplierProducerProduct.supplier_id == supplier_id)).all()
        self.session.close()
        return result
