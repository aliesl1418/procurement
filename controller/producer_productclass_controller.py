from controller import *
from model.da import *
from model.entity import *


class ProducerProductClassController:
    @classmethod
    def save(cls, omniclass_code, producer_id):
        try:
            da = ProducerProductClassDa()
            if not (da.find_by_omniclass_code_and_producer_id(omniclass_code, producer_id)):
                producer_product = ProducerProductClass(omniclass_code, producer_id)
                da.save(producer_product)
                return producer_product
            else:
                raise DuplicateUsernameError("Duplicate producer_product")
        except Exception as e:
            e.with_traceback()
            return False, str(e)

    @classmethod
    def edit(cls, id, omniclass_code, producer_id):
        try:
            da = ProducerProductClassDa()
            producer_product = ProducerProductClass(omniclass_code, producer_id)
            producer_product.id = id
            da.edit(producer_product)
            return producer_product
        except Exception as e:
            e.with_traceback()
            return False, str(e)
    @classmethod
    def remove(cls, id):
        try:
            da = ProducerProductClassDa()
            producer_product = da.find_by_id(ProducerProductClass, id)
            return da.remove(producer_product)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            da = ProducerProductClassDa()
            return da.find_all(ProducerProductClass)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_producer_id(cls, producer_id):
        try:
            da = ProducerProductClassDa()
            result = da.find_by_producer_id(producer_id)
            if result:
                return result
        except Exception as e:
            return False, str(e)
    @classmethod
    def find_by_omniclass_code(cls, omniclass_code):
        try:
            da = ProducerProductClassDa()
            result = da.find_by_omniclass_code(omniclass_code)
            if result:
                return result
        except Exception as e:
            return False, str(e)