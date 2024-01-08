# model/entity/profile.py
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean
from sqlalchemy.orm import relationship
from model.entity.base import Base


# from model.da.product_classification_da import ProductClassificationDa
# import pandas as pd
# from sqlalchemy import create_engine, Column, Integer, String,Boolean
# from sqlalchemy.ext.declarative import declarative_base


class RequiredProduct(Base):
    __tablename__ = "requiredproduct_tbl"

    # افزودن پارامتر extend_existing=True
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    projectclient_id = Column(Integer, ForeignKey("projectclient_tbl.id"))
    omniclass_code = Column(String(50), ForeignKey("productclassification_tbl.omniclass_code"))
    count = Column(Integer)
    Color = Column(String(30))
    Height = Column(Float)
    Length = Column(Float)
    Width = Column(Float)
    Depth = Column(Float)
    Thickness = Column(Float)
    Material = Column(String(30))
    Weight = Column(Float)
    ManufacturerFa = Column(String(50))
    Manufacturer = Column(String(30))
    ModelLabel = Column(String(30))
    status = Column(Boolean)
    description = Column(String(300))

    projectclient_r = relationship("ProjectClient", back_populates="requiredproduct_r")
    omniclass_code_r = relationship("ProductClassification", back_populates="requiredproduct_r")
    callprice_r = relationship("CallPrice", back_populates="requiredproduct_r")

    def __init__(self, projectclient_id, omniclass_code, count, Color, Height, Length, Width, Depth, Thickness,
                 Material, Weight, ManufacturerFa, Manufacturer, ModelLabel, description=None, status=False):
        super().__init__()
        self.projectclient_id = projectclient_id
        self.omniclass_code = omniclass_code
        self.count = count
        self.Color = Color
        self.Height = Height
        self.Length = Length
        self.Width = Width
        self.Depth = Depth
        self.Thickness = Thickness
        self.Material = Material
        self.Weight = Weight
        self.ManufacturerFa = ManufacturerFa
        self.Manufacturer = Manufacturer
        self.ModelLabel = ModelLabel
        self.description = description
        self.status = status
