import os
import pandas as pd
from sqlalchemy import text
from dw.conection import get_engine
from extract import extract
from transform import Fact_Sales

def truncate_table(engine):
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, "..", "data", "tables")
    
    with engine.begin() as conn:
        for file_name in os.listdir(data_path):    
            if file_name.endswith(".csv"):
                try:
                    rename_file = file_name.replace(".csv","")
                    conn.execute(text(f"TRUNCATE TABLE {rename_file};"))
                except Exception as ex:
                    print(f'Error Truncado: {ex}')

    

def Save_Dw():
    engine = get_engine()
    truncate_table(engine)
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, "..", "data", "tables")
    
    for file_name in os.listdir(data_path):    
        if file_name.endswith(".csv") and not file_name.startswith("Fact"):
            try:
                rename_file = file_name.replace(".csv","")
                file_path = os.path.join(data_path, file_name)
                
                df = pd.read_csv(file_path)
                df.to_sql(rename_file, engine, if_exists="append", index=False)
            except Exception as ex:
                print(f'Error en Insercion: {ex}')

    try:
        df = extract()
        Fact_Sales(df)
    except Exception as ex:
        print(f'Problema en fact_load {ex}')
    
    #insertamos ya el fact Sales
    try:
        for file_name in os.listdir(data_path):    
            if file_name.startswith("Fact_Sales") :
           
                rename_file = file_name.replace(".csv","")
                file_path = os.path.join(data_path, file_name)
                
                df = pd.read_csv(file_path)                
                df.to_sql(rename_file, engine, if_exists="append", index=False)
    except Exception as ex:
        print(f'Problema en fact_load {ex}')