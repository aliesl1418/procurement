# model/entity/post.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime,Float, func
from sqlalchemy.orm import relationship
from datetime import datetime
from model.entity.base import Base

class CallPrice(Base):
    __tablename__ = "callprice_tbl"

    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    requiredproduct_id = Column(Integer, ForeignKey("requiredproduct_tbl.id"))
    suppliar_id = Column(Integer, ForeignKey("supplier_tbl.id"))
    producer_id = Column(Integer, ForeignKey("producer_tbl.id"))
    timeofcallprice = Column(DateTime, default=datetime.now())
    u_price = Column(Float)
    t_price = Column(Float)
    timeofresponse = Column(DateTime(timezone=True), onupdate=func.now())
    description = Column(String(300))

    requiredproduct_r = relationship("CallPrice", back_populates="callprice_r")
    supplier_r = relationship("Supplier", back_populates="callprice_r")
    producer_r = relationship("Producer", back_populates="callprice_r")


    def __init__(self, requiredproduct_id, u_price, t_price, description ,suppliar_id=None, producer_id=None):
        self.requiredproduct_id = requiredproduct_id
        self.suppliar_id = suppliar_id
        self.producer_id = producer_id
        self.u_price = u_price
        self.t_price = t_price
        self.description = description
