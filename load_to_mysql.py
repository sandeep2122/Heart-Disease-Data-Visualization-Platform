import pandas as pd
from sqlalchemy import create_engine

# ==========================================
# MySQL Configuration Variables
# Please update these to match your local setup
# ==========================================
USERNAME = 'root'
PASSWORD = 'password'  # Replace with your actual MySQL root password
HOST = 'localhost'
DATABASE = 'heart_disease_db'  # You must create this schema in MySQL Workbench first!

def load_to_mysql():
    print(f"Attempting to connect to MySQL database '{DATABASE}' at {HOST}...")
    
    # Create the SQLAlchemy engine using pymysql
    # Note: Requires running `pip install sqlalchemy pymysql` in your terminal
    try:
        engine = create_engine(f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}')
        
        # 1. Load Data
        csv_path = 'heart_disease_tableau_final.csv'
        print(f"Reading {csv_path}...")
        df = pd.read_csv(csv_path)
        
        # 2. Push to MySQL
        table_name = 'heart_data'
        print(f"Writing {len(df)} rows and {len(df.columns)} columns to MySQL table '{table_name}'...")
        
        # This will create the table automatically and insert the data
        df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)
        
        print("Data successfully loaded into MySQL!")
        print("You can now open MySQL Workbench to verify the volume and columns.")
        
    except Exception as e:
        print("\n[ERROR] Failed to connect or upload to MySQL.")
        print(f"Details: {e}")
        print("\nMake sure you have:")
        print("1. Started your MySQL Server.")
        print("2. Updated the PASSWORD variable in this script.")
        print("3. Created a schema named 'heart_disease_db' in MySQL Workbench.")

if __name__ == '__main__':
    load_to_mysql()
