# model/entity/profile.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model.entity.base import Base


# from model.da.producer_da import producerDa

class ProducerProductClass(Base):
    __tablename__ = "producerproductclass_tbl"

    # افزودن پارامتر extend_existing=True
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    omniclass_code = Column(String(50), ForeignKey("productclassification_tbl.omniclass_code"))
    producer_id = Column(Integer, ForeignKey("producer_tbl.id"))

    omniclass_code_r = relationship("ProductClassification", back_populates="producerproductclass_r")
    producer_r = relationship("Producer", back_populates="producerproductclass_r")
    supplierproducerproduct_r = relationship("SupplierProducerProduct", back_populates="producerproductclass_r")
    def __init__(self, omniclass_code, producer_id):
        super().__init__()
        self.omniclass_code = omniclass_code
        self.producer_id = producer_id
