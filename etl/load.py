import os
import pandas as pd
from dw.conection import get_engine



def Save_Dw():
    engine = get_engine()
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, "..", "data", "tables")
    
    for file_name in os.listdir(data_path):    
        if file_name.endswith(".csv") and not file_name.startswith("Fact"):
            rename_file = file_name.replace(".csv","")
            file_path = os.path.join(data_path, file_name)
            print(file_path)
            
            df = pd.read_csv(file_path)
            
            
            df.to_sql(rename_file, engine, if_exists="append", index=False)
            print("Ejecucion correcta")
            print("Ejecucion correcta")
