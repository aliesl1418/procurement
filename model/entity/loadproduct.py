from model.da.product_classification_da import ProductClassificationDa
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model.entity.required_product import RequiredProduct
from model.entity import Base

engine = create_engine("mysql+pymysql://root:root123@localhost:3306/mft", echo=True)
connection = engine.connect()
Base.metadata.create_all(engine)

df = pd.read_csv(r'C:\NLBO\table.csv')
#برای اینکه رکوردهای خالی حذف شوند کد زیر را نوشتم
df.dropna(inplace=True)
df['status'] = False
df['description'] = "Nothing"
df.to_sql('requiredproduct_tbl', con=engine, if_exists='append', index=False)
