import pandas as pd
import os

def extract():
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    data_path = os.path.join(base_dir, "..", "data", "raw", "SampleSuperstore.csv")
    df = pd.read_csv(data_path, encoding='latin-1')
    

    #Realizamos la Limpieza y renombrar algunas columnas y cambios en las fechas
    df.rename(columns={
    'Row ID': 'Row_ID',
    'Order ID': 'Order_ID',
    'Order Date': 'Order_Date',
    'Ship Date':'Ship_Date',
    'Ship Mode':'Ship_Mode',
    'Customer ID':'Customer_ID',
    'Customer Name':'Customer_Name',
    'Postal Code':'Postal_Code',
    'Product ID':'Product_Code',
    'Product Name':'Product_Name',
    'Sub-Category':'Sub_Category'
    }, inplace=True)
    
    #cambiamos los tipos de datos de fecha a datetime
    df['Order_Date'] = pd.to_datetime(df['Order_Date'])
    df['Ship_Date'] = pd.to_datetime(df['Ship_Date'])
    return df


