from controller import *
from model.da import *
from model.entity import *


class SupplierProducerProductController:
    @classmethod
    def save(cls, producerproductclass_id, supplier_id):
        try:
            da = SupplierProducerProductDa()
            if not (da.find_by_supplier_and_producer_productclass(producerproductclass_id, supplier_id)):
                supplier_producer_product = SupplierProducerProduct(producerproductclass_id, supplier_id)
                da.save(supplier_producer_product)
                return supplier_producer_product
            else:
                raise DuplicateUsernameError("Duplicate supplierproducerproduct")
        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, producerproductclass_id, supplier_id):
        try:
            da = SupplierProducerProductDa()
            supplier_producer_product = SupplierProducerProduct(producerproductclass_id, supplier_id)
            supplier_producer_product.id = id
            da.edit(supplier_producer_product)
            return supplier_producer_product
        except Exception as e:
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = SupplierProducerProductDa()
            supplier_producer_product = da.find_by_id(SupplierProducerProduct, id)
            return da.remove(supplier_producer_product)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            da = SupplierProducerProductDa()
            return da.find_all(SupplierProducerProduct)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, supplier_producer_product_id):
        try:
            da = SupplierProducerProductDa()
            result = da.find_by_id(SupplierProducerProduct, supplier_producer_product_id)
            if result:
                return result
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_supplier_id(cls, supplier_id):
        try:
            da = SupplierProducerProductDa()
            result = da.find_by_supplier_id(supplier_id)
            if result:
                return result
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_producer_name_and_omniclass_code(cls, producer_name, omniclass_code):
        try:
            da = SupplierProducerProductDa()
            result = da.find_by_producer_name_and_omniclass_code(producer_name, omniclass_code)
            if result:
                return result
        except Exception as e:
            return False, str(e)
