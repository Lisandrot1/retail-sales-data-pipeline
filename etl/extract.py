import pandas as pd
import os

def extract():
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    data_path = os.path.join(base_dir, "..", "data", "raw", "SampleSuperstore.csv")
    df = pd.read_csv(data_path, encoding='latin-1')
    return df
