# coding=utf-8
import os
import pyodbc

from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import URL

db_url = 'localhost:1443'
db_name = 'master'
db_user = 'sa'
db_password = '{{pw}}'

url_object = URL.create(
    "mssql+pyodbc",
    username=db_user,
    password=db_password,  # plain (unescaped) text
    host=db_url,
    database=db_name,
)
connection = "Driver={ODBC Driver 18 for SQL Server};Server=tcp:servertestpyodbccon.database.windows.net,1433;Database=rmbgtstpyodbc;Uid=rmbgadmin;Pwd={{pw}};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
cnxn = pyodbc.connect(connection)
engine = create_engine("mssql+pyodbc://rmbgadmin:{{pw}}@servertestpyodbccon.database.windows.net:1433/rmbgtstpyodbc?driver=ODBC+Driver+18+for+SQL+Server")
Session = sessionmaker(bind=engine)

Base = declarative_base()

Session = "dummy"
engine = "dummy"
Base = "dummy"
