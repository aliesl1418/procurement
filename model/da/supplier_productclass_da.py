from model.da.database import DataBaseManager, and_, or_, between
from model.entity import *


class SupplierProductClassDa(DataBaseManager):
    def find_by_omniclasscode(self, omniclass_code):
        self.make_engine()
        result = self.session.query(SupplierProductClass).filter(
            SupplierProductClass.omniclass_code == omniclass_code).all()
        for row in result:
            if self.session.query(Supplier).filter(Supplier.id == row.suppliar_id):
                x = self.session.query(Supplier).filter(Supplier.id == row.suppliar_id)
        self.session.close()
        return x

    # def find_by_supplier_id(self, supplier_id):
    #     self.make_engine()
    #     result = self.session.query(SupplierProductClass).filter(
    #         SupplierProductClass.supplier_id == supplier_id).all()
    #     for row in result:
    #         if self.session.query(ProductClassification).filter(ProductClassification.omniclass_code == row.omniclass_code):
    #             x = self.session.query(ProductClassification).filter(ProductClassification.omniclass_code == row.omniclass_code)
    #     self.session.close()
    #     return x
    def find_by_omniclass_code_and_supplier_id(self, omniclass_code, supplier_id):
        self.make_engine()
        result = self.session.query(SupplierProductClass).filter(and_(
            SupplierProductClass.omniclass_code == omniclass_code,
            SupplierProductClass.supplier_id == supplier_id)).all()
        if result:
            return result
    def find_by_supplier_id(self, supplier_id):
        self.make_engine()
        result = self.session.query(SupplierProductClass).filter(
            SupplierProductClass.supplier_id == supplier_id).all()
        return result

    def find_by_omniclass_code(self, omniclass_code):
        self.make_engine()
        result = self.session.query(SupplierProductClass).filter(
            SupplierProductClass.omniclass_code == omniclass_code).all()
        return result


