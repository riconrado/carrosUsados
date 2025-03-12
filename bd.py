from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

from flask import g

# Carrega as variáveis do arquivo .env
load_dotenv()

host = os.getenv('DATABASE_HOST')
user = os.getenv('DATABASE_USER')
password = os.getenv('DATABASE_PASSWORD')
database = os.getenv('DATABASE_NAME')
port = os.getenv('DATABASE_PORT')

# Create the database URL
database_url = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"

try:
    # Create the SQLAlchemy engine
    engine = create_engine(database_url)

    conn = engine.connect()
    # query = text("SELECT version();")
    # query = text("SELECT marca,modelo,ano,preco FROM veiculos LIMIT 10")

    # exe = conn.execute(query) #executing the query
    # result = exe.fetchall()
    # print(result)
    # print(jsonify(result))
    
except SQLAlchemyError as e:
    print(f"Ocorreu um erro na criação da engine: {e}")