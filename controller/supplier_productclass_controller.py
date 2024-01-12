from controller import *
from model.da import *
from model.entity import *


class SupplierProductClassController:
    @classmethod
    def save(cls, omniclass_code, supplier_id):
        try:
            da = SupplierProductClassDa()
            if not (da.find_by_omniclass_code_and_supplier_id(omniclass_code, supplier_id)):
                supplier_product = SupplierProductClass(omniclass_code, supplier_id)
                da.save(supplier_product)
                return supplier_product
            else:
                raise DuplicateUsernameError("Duplicate supplier_product")
        except Exception as e:
            e.with_traceback()
            return False, str(e)

    @classmethod
    def edit(cls, id, omniclass_code, supplier_id):
        try:
            da = SupplierProductClassDa()
            supplier_product = SupplierProductClass(omniclass_code, supplier_id)
            supplier_product.id = id
            da.edit(supplier_product)
            return supplier_product
        except Exception as e:
            e.with_traceback()
            return False, str(e)
    @classmethod
    def remove(cls, id):
        try:
            da = SupplierProductClassDa()
            supplier_product = da.find_by_id(SupplierProductClass, id)
            return da.remove(supplier_product)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            da = SupplierProductClassDa()
            return da.find_all(SupplierProductClass)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_supplier_id(cls, supplier_id):
        try:
            da = SupplierProductClassDa()
            result = da.find_by_supplier_id(supplier_id)
            if result:
                return result
        except Exception as e:
            return False, str(e)
    @classmethod
    def find_by_omniclass_code(cls, omniclass_code):
        try:
            da = SupplierProductClassDa()
            result = da.find_by_omniclass_code(omniclass_code)
            if result:
                return result
        except Exception as e:
            return False, str(e)