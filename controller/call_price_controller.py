from controller import *
from model.da import *
from model.entity import *


class CallPriceController:
    @classmethod
    def save_supplier(cls, requiredproduct_id, u_price, t_price, supplier_id, description):
        try:
            da = CallPriceDa()
            if not da.find_unique_for_supplier(requiredproduct_id, supplier_id):
                callprice = CallPrice(requiredproduct_id, u_price, t_price, supplier_id=supplier_id,
                                      description=description)
                da.save(callprice)
                return callprice
            else:
                raise DuplicateUsernameError("Duplicate  callprice")

        except Exception as e:
            return False, str(e)

    @classmethod
    def save_producer(cls, requiredproduct_id, u_price, t_price, producer_id, description):
        try:
            da = CallPriceDa()
            if not da.find_unique_for_producer(requiredproduct_id, producer_id):
                callprice = CallPrice(requiredproduct_id, u_price, t_price, producer_id=producer_id,
                                      description=description)
                da.save(callprice)
                return callprice
            else:
                raise DuplicateUsernameError("Duplicate  callprice")

        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, requiredproduct_id, u_price, t_price, description, supplier_id):
        try:
            da = CallPriceDa()
            callprice = CallPrice(requiredproduct_id, u_price, t_price, description=description,
                                  supplier_id=supplier_id)
            callprice.id = id
            da.edit(callprice)
            return callprice
        except Exception as e:
            e.with_traceback()
            return False, str(e)

    @classmethod
    def edit_status(cls, item_id):
        try:
            da = CallPriceDa()
            callprice = da.edit_status(item_id)
            return callprice
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit_description(cls, item_id, description):
        try:
            da = CallPriceDa()
            callprice = da.edit_description(item_id, description)
            return callprice
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = CallPriceDa()
            callprice = da.find_by_id(CallPrice, id)
            return da.remove(callprice)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            da = CallPriceDa()
            return da.find_all(CallPrice)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            da = CallPriceDa()
            callprice = da.find_by_id(CallPrice, id)
            if callprice:
                return callprice
            else:
                raise NoContentError("There is no callprice!")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_requiredproduct(cls, requiredproduct_id):
        try:
            da = CallPriceDa()
            callprice = da.find_by_requiredproduct(requiredproduct_id)
            return callprice
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_supplier_id(cls, supplier_id):
        try:
            da = CallPriceDa()
            callprice = da.find_by_supplier_id(supplier_id)
            return callprice
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_producer_id(cls, producer_id):
        try:
            da = CallPriceDa()
            callprice = da.find_by_producer_id(producer_id)
            return callprice
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_status(cls, status):
        try:
            da = CallPriceDa()
            callprice = da.find_by_status(status)
            return callprice
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_callprice_for_client(self, client_id):
        try:
            da = CallPriceDa()
            callprice = da.find_callprice_for_client(client_id)
            return callprice
        except Exception as e:
            return False, str(e)
