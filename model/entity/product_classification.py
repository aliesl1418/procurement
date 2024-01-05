# model/entity/profile.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from model.entity.base import Base
# from model.da.product_classification_da import ProductClassificationDa
# import pandas as pd
# from sqlalchemy import create_engine, Column, Integer, String,create_engine
# from sqlalchemy.ext.declarative import declarative_base



class ProductClassification(Base):
    __tablename__ = "productclassification_tbl"

    # افزودن پارامتر extend_existing=True
    __table_args__ = {'extend_existing': True}

    omniclass_code = Column(String(50),primary_key=True)
    omniclass_name = Column(String(200))
    omniclass_level = Column(String(30))

    requiredproduct_r = relationship("RequiredProduct", back_populates="omniclass_code_r")
    supplierproductclass_r = relationship("SupplierProductClass", back_populates="omniclass_code_r")
    producerproductclass_r = relationship("ProducerProductClass", back_populates="omniclass_code_r")

    def __init__(self,omniclass_code,omniclass_name,omniclass_level):
        super().__init__()
        self.omniclass_code = omniclass_code
        self.omniclass_name = omniclass_name
        self.omniclass_level = omniclass_level



# engine = create_engine("mysql+pymysql://root:root123@localhost:3306/mft", echo=True)
# connection = engine.connect()
# Base.metadata.create_all(engine)
# df = pd.read_csv(r'C:\NLBO\omni.txt', delimiter='\t')
# df.to_sql('productclassification_tbl', con=engine, if_exists='append',index=False)
# # # باید برویم در دیتابیس و مقادیر ستون و کلید اصلی را مشخص کنیم




