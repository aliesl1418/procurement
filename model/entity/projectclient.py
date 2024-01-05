# model/entity/profile.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model.entity.base import Base


# from model.da.supplier_da import SupplierDa

class ProjectClient(Base):
    __tablename__ = "projectclient_tbl"

    # افزودن پارامتر extend_existing=True
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey("client_tbl.id"))
    project_id = Column(Integer, ForeignKey("project_tbl.id"))

    project_r = relationship("Project", back_populates="projectclient_r")
    client_r = relationship("Client", back_populates="projectclient_r")
    requiredproduct_r = relationship("RequiredProduct", back_populates="projectclient_r")

    def __init__(self, client_id, project_id):
        super().__init__()
        self.client_id = client_id
        self.project_id = project_id

# da = SupplierDa()
# supplier = Supplier('ALI','ESLAMI','09392065637','AESLAMIFARGHJ@GMAIL.COM','dress','useme','passord')
# da.save(supplier)
