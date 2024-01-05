# model/entity/profile.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model.entity.base import Base


# from model.da.supplier_da import SupplierDa

class SupplierProducerProduct(Base):
    __tablename__ = "supplierproducerproduct_tbl"

    # افزودن پارامتر extend_existing=True
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    producerproductclass_id = Column(String(50), ForeignKey("producerproductclass_tbl.id"))
    supplier_id = Column(Integer, ForeignKey("supplier_tbl.id"))

    producerproductclass_r = relationship("ProducerProductClass", back_populates="supplierproducerproduct_r")
    supplier_r = relationship("Supplier", back_populates="supplierproducerproduct_r")

    def __init__(self, producerproductclass_id, supplier_id):
        super().__init__()
        self.producerproductclass_id = producerproductclass_id
        self.supplier_id = supplier_id
