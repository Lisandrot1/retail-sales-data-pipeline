import pyodbc
from dotenv import dotenv_values

def connection():
    config = dotenv_values('.env')
    SERVER = config.get('DB_HOST') 
    DATABASE = config.get('DB_NAME') 
    USERNAME = config.get('DB_USER') 
    PASSWORD = config.get('DB_PASS')
    try:
        connection = pyodbc.connect(
        f"DRIVER={{SQL Server}};"
        f"SERVER={SERVER};"
        f"DATABASE={DATABASE};"
        f"UID={USERNAME};"
        f"PWD={PASSWORD};"
    )
        print("Conexion exitosa")
        return connection
    except Exception as ex:
        print(ex)
