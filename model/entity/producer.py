# model/entity/profile.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model.entity.base import Base
# from model.da.producer_da import ProducerDa

class Producer(Base):
    __tablename__ = "producer_tbl"

    # افزودن پارامتر extend_existing=True
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    family = Column(String(30))
    phonenumber = Column(String(30))
    email = Column(String(30))
    address = Column(String(200))
    username = Column(String(30))
    password = Column(String(30))

    callprice_r = relationship("CallPrice", back_populates="producer_r")
    producerproductclass_r = relationship("ProducerProductClass", back_populates="producer_r")


    def __init__(self, name, family,phonenumber,email,address , username, password):
        super().__init__()
        self.name = name
        self.family = family
        self.phonenumber = phonenumber
        self.email = email
        self.address = address
        self.username = username
        self.password = password

# da = ProducerDa()
# x = Producer('ALI','ESLAMI','09392065637','AESLAMIFARGHJ@GMAIL.COM','dress','useme','passord')
# da.save(x)
