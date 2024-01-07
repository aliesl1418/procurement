from model.da.database import DataBaseManager, and_, or_, between
from model.entity import *


class CallPriceDa(DataBaseManager):
    def find_by_requiredproduct(self, requiredproduct_id):
        self.make_engine()
        result = self.session.query(CallPrice).filter(CallPrice.requiredproduct_id == requiredproduct_id)
        self.session.close()
        return result

    def find_by_supplier_id(self, supplier_id):
        self.make_engine()
        result = self.session.query(CallPrice).filter(CallPrice.supplier_r == supplier_id)
        self.session.close()
        return result

    def find_by_producer_id(self, producer_id):
        self.make_engine()
        result = self.session.query(CallPrice).filter(CallPrice.producer_id == producer_id)
        self.session.close()
        return result

    def find_by_status(self, status):
        self.make_engine()
        result = self.session.query(CallPrice).filter(CallPrice.status == status)
        self.session.close()
        return result
