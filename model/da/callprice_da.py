from model.da.database import DataBaseManager, and_, or_, between
from model.entity import *


class CallPriceDa(DataBaseManager):
    def find_by_requiredproduct(self, requiredproduct_id):
        self.make_engine()
        result = self.session.query(CallPrice).filter(CallPrice.requiredproduct_id == requiredproduct_id).all()
        self.session.close()
        return result

    def find_by_supplier_id(self, supplier_id):
        self.make_engine()
        result = self.session.query(CallPrice).filter(CallPrice.supplier_id == supplier_id).all()
        self.session.close()
        return result

    def find_by_producer_id(self, producer_id):
        self.make_engine()
        result = self.session.query(CallPrice).filter(CallPrice.producer_id == producer_id).all()
        self.session.close()
        return result

    def find_by_status(self, status):
        self.make_engine()
        result = self.session.query(CallPrice).filter(CallPrice.status == status).all()
        self.session.close()
        return result

    def find_callprice_for_client(self, client_id):
        self.make_engine()
        result = self.session.query(CallPrice).join(CallPrice.requiredproduct_r). \
            join(RequiredProduct.projectclient_r).join(ProjectClient.client_r).filter(Client.id == client_id).all()
        self.session.close()
        return result

    def find_unique_for_supplier(self, requiredproduct_id, supplier_id):
        self.make_engine()
        result = self.session.query(CallPrice). \
            filter(and_(CallPrice.supplier_id == supplier_id, CallPrice.requiredproduct_id == requiredproduct_id)).all()
        self.session.close()
        return result

    def find_unique_for_producer(self, requiredproduct_id, producer_id):
        self.make_engine()
        result = self.session.query(CallPrice). \
            filter(and_(CallPrice.producer_id == producer_id, CallPrice.requiredproduct_id == requiredproduct_id)).all()
        self.session.close()
        return result

    def edit_status(self, item_id):
        self.make_engine()
        entity = self.session.get(CallPrice, item_id)
        if not entity.status:
            change = CallPrice(entity.requiredproduct_id, entity.u_price, entity.t_price, status=True,
                               supplier_id=entity.supplier_id,description=entity.description,producer_id=entity.producer_id)
        else:
            change = CallPrice(entity.requiredproduct_id, entity.u_price, entity.t_price, status=False,
                               supplier_id=entity.supplier_id,description=entity.description,producer_id=entity.producer_id)
        change.id = entity.id
        self.session.merge(change)
        self.session.commit()
        return change

    def edit_description(self, item_id, description):
        self.make_engine()
        entity = self.session.get(CallPrice, item_id)
        if not entity.status:
            change = CallPrice(entity.requiredproduct_id, entity.u_price, entity.t_price, description=description)
        else:
            change = CallPrice(entity.requiredproduct_id, entity.u_price, entity.t_price, description=description)
        change.id = entity.id
        self.session.merge(change)
        self.session.commit()
        return change
