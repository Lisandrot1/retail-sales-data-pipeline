import pandas as pd
from extract import extract
from dw.conection import get_engine
import os

df = extract()

def base_dir(file_name):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, "..", "data", "tables", file_name)
    
    return data_path


def save_data(df, output_file_name, index=False):
    pathComplete = base_dir(output_file_name)
    df.to_csv(pathComplete, index=index)
    print("Archivo guardado!")



def Dim_Customer(df):
        customers = df[['Customer_Code','Customer_Name','Segment']].drop_duplicates(subset=['Customer_Code'],keep='first')
        save_data(
            df=customers,
            output_file_name='Dim_Customer.csv'
        )
       

def Dim_Products(df):
    products = df[['Product_Code','Product_Name']].drop_duplicates(subset=['Product_Code'], keep='first')    
    save_data(
        df=products,
        output_file_name='Dim_Products.csv'
    )
    


def Dim_Geography (df):
    geography = df[['City','State','Country','Region','Postal_Code']].drop_duplicates(subset=['City'],keep='first')
    save_data(
        df=geography,
        output_file_name='Dim_Geography.csv'
    )

def Dim_Category(df):
    category= df[['Category']].drop_duplicates()
    save_data(
        df=category,
        output_file_name='Dim_Category.csv'
    )

def Dim_SubCategory(df):
    subcategory = df[['Sub_Category']].drop_duplicates()
    save_data(
        df=subcategory,
        output_file_name='Dim_SubCategory.csv'
    )

def Fact_Sales(df):
    engine = get_engine()
    #traer ids de las dimensiones
    idcustomer = pd.read_sql('SELECT Customer_ID,Customer_Code FROM Dim_Customer',engine)
    idproduct = pd.read_sql('SELECT Product_ID,Product_Code FROM Dim_Products', engine)
    idgeography = pd.read_sql('SELECT Geography_ID,City FROM Dim_Geography', engine)
    idcategory = pd.read_sql('SELECT Category_ID,Category FROM Dim_Category', engine)
    idsubcategory = pd.read_sql('SELECT SubCategory_ID,Sub_Category FROM Dim_SubCategory', engine)

    df = df.merge(idcustomer, on='Customer_Code', how='left')
    df = df.merge(idproduct, on='Product_Code', how='left')
    df = df.merge(idgeography, on='City', how='left')
    df = df.merge(idcategory, on='Category', how='left')
    df = df.merge(idsubcategory, on='Sub_Category', how='left')
    
    sales = df[[
        'Order_ID','Order_Date','Ship_Date','Ship_Mode','Customer_ID',
        'Product_ID','Category_ID','SubCategory_ID','Geography_ID','Sales','Quantity','Discount','Profit']]
    
    save_data(
        df=sales,
        output_file_name='Fact_Sales.csv'
    )



def main():
    try:
        df = extract()
        Dim_Customer(df)
        Dim_Products(df)
        Dim_Geography(df)
        Dim_Category(df)
        Dim_SubCategory(df)
    except Exception as ex:
        print(f'Ocurrio un problema en {ex}')



