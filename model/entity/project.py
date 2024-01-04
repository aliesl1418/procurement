# model/entity/profile.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model.entity.base import Base
# from model.da.supplier_da import SupplierDa

class Project(Base):
    __tablename__ = "project_tbl"

    # افزودن پارامتر extend_existing=True
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    phonenumber = Column(String(30))
    email = Column(String(30))
    address = Column(String(200))

    projectclient_r = relationship("model.entity.projectclient.ProjectClient", back_populates="project_r")

    # producer_classification = relationship("ProducerClassification", back_populates="producer")

    def __init__(self, name,phonenumber,email,address):
        super().__init__()
        self.name = name
        self.phonenumber = phonenumber
        self.email = email
        self.address = address


# da = SupplierDa()
# supplier = Supplier('ALI','ESLAMI','09392065637','AESLAMIFARGHJ@GMAIL.COM','dress','useme','passord')
# da.save(supplier)
