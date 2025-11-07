from sqlalchemy import create_engine
from dotenv import dotenv_values

def get_engine():
    config = dotenv_values('.env')
    SERVER = config.get('DB_HOST')
    DATABASE = config.get('DB_NAME')
    USERNAME = config.get('DB_USER')
    PASSWORD = config.get('DB_PASS')

    # URL de conexión para SQL Server con pyodbc
    connection_url = (
        f"mssql+pyodbc://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}"
        "?driver=ODBC+Driver+17+for+SQL+Server"
    )

    try:
        engine = create_engine(connection_url)
        print("✅ Conexión exitosa con SQLAlchemy")
        return engine
    except Exception as ex:
        print(f"❌ Error al conectar: {ex}")


get_engine()