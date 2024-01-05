# model/entity/profile.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model.entity.base import Base


# from model.da.supplier_da import SupplierDa

class SupplierProductClass(Base):
    __tablename__ = "supplierproductclass_tbl"

    # افزودن پارامتر extend_existing=True
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    omniclass_code = Column(String(50), ForeignKey("productclassification_tbl.omniclass_code"))
    supplier_id = Column(Integer, ForeignKey("supplier_tbl.id"))

    omniclass_code_r = relationship("ProductClassification", back_populates="supplierproductclass_r")
    supplier_r = relationship("Supplier", back_populates="supplierproductclass_r")

    def __init__(self, omniclass_code, supplier_id):
        super().__init__()
        self.omniclass_code = omniclass_code
        self.supplier_id = supplier_id