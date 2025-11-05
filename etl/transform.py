import pandas as pd
from extract import extract

def transform():
    #traemos el dataframe de la extracion para la limpieza
    df = extract()
    # vamos a renombrar algunas columnas dentro del dataset
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


def Dim_Customer(df):
    pass


def Dim_Products(df):
    pass


def Dim_Geography (df):
    pass




def main():
    try:
        transform()
        Dim_Customer()
        Dim_Products()
        Dim_Geography()
    except Exception as ex:
        print(f'Ocurrio un problema en {ex}')
        
        
if __name__ == "__main__":
    main()  