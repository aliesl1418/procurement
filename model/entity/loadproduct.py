import os

from model.da.product_classification_da import ProductClassificationDa
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model.entity.required_product import RequiredProduct
from model.entity import Base


def load():
    if os.path.exists("c:/NLBO/table.csv"):
        engine = create_engine("mysql+pymysql://root:root123@localhost:3306/mft")
        Base.metadata.create_all(engine)
        df = pd.read_csv('C:/NLBO/table.csv')
        print(df)
        # df.dropna(inplace=True)
        df['status'] = False
        df['description'] = "Nothing"
        df.to_sql('requiredproduct_tbl', con=engine, if_exists='append', index=False)
        os.remove("c:/NLBO/table.csv")




