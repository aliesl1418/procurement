from controller import *
from model.da import *
from model.entity import *


class SupplierController:
    @classmethod
    def save(cls, name, family, phonenumber, email, address, username, password):
        try:
            da = SupplierDa()
            if not da.find_by_username(username):
                supplier = Supplier(name, family, phonenumber, email, address, username, password)
                da.save(supplier)
                return supplier
            else:
                raise DuplicateUsernameError("Duplicate Username")

        except Exception as e:
            return False, str(e)

    @classmethod
    def edit(cls, id, name, family, phonenumber, email, address, username, password):
        try:
            da = SupplierDa()
            supplier = Supplier(name, family, phonenumber, email, address, username, password)
            supplier.id = id
            da.edit(supplier)
            return supplier
        except Exception as e:
            e.with_traceback()
            return False, str(e)

    @classmethod
    def remove(cls, id):
        try:
            da = SupplierDa()
            supplier = da.find_by_id(Supplier, id)
            return da.remove(supplier)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_all(cls):
        try:
            da = SupplierDa()
            return da.find_all(Supplier)
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_id(cls, id):
        try:
            da = SupplierDa()
            supplier = da.find_by_id(Supplier, id)
            if supplier:
                return supplier
            else:
                raise NoContentError("There is no profile!")
        except Exception as e:
            return False, str(e)

    @classmethod
    def find_by_username(cls, username):
        try:
            da = SupplierDa()
            return da.find_by_username(username)
        except Exception as e:
            return False, str(e)

    @classmethod
    def login(cls, username, password):
        try:
            da = SupplierDa()
            supplier = da.find_by_username_password(username, password)
            if supplier:
                return supplier
            else:
                raise AccessDeniedError("Wrong username/password")
        except Exception as e:
            return False, str(e)
