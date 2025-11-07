import pandas as pd
from extract import extract
import os

df = extract()

def base_dir(file_name):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, "..", "data", "tables", file_name)
    
    return data_path


def save_data(df, output_file_name, index=False):
    pathComplete = base_dir(output_file_name)
    df.to_csv(pathComplete, index=index)
    print("Archivo guardado")



def Dim_Customer(df):
        customers = df[['Customer_ID','Customer_Name','Segment']].drop_duplicates()
        save_data(
            df=customers,
            output_file_name='Dim_Customer.csv'
        )
       

def Dim_Products(df):
    products = df[['Product_Code','Product_Name','Category','Sub_Category']].drop_duplicates()
    
    save_data(
        df=products,
        output_file_name='Dim_Products.csv'
    )
    


def Dim_Geography (df):
    geography = df[['City','State','Country','Region','Postal_Code']].drop_duplicates()
    save_data(
        df=geography,
        output_file_name='Dim_Geography.csv'
    )


def Fact_Sales(df):
    pass

def main():
    try:
        df = extract()
        Dim_Customer(df)
        Dim_Products(df)
        Dim_Geography(df)
        Fact_Sales(df)
    except Exception as ex:
        print(f'Ocurrio un problema en {ex}')
        
        
if __name__ == "__main__":
    main()  