from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv
import os

# Carrega as variáveis do arquivo .env
load_dotenv()

# Lê as variáveis
usuario = os.getenv("DB_USER")
senha = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
porta = os.getenv("DB_PORT")
banco = os.getenv("DB_NAME")

# Monta a URL de conexão
DATABASE_URL = f'mysql+mysqlconnector://{usuario}:{senha}@{host}:{porta}/{banco}'

# Cria a engine
engine = create_engine(DATABASE_URL)

# Testa a conexão
try:
    with engine.connect() as conexao:
        resultado = conexao.execute(text("SELECT 1"))
        for row in resultado:
            print("✅ Conexão bem-sucedida!", row)
except SQLAlchemyError as e:
    print("❌ Erro ao conectar no banco de dados:", e)
