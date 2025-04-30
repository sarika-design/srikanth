import pandas as pd
import pyodbc

# Define connection parameters
server = 'SARIKA'  # Example: 'DESKTOP-XXXX\SQLEXPRESS' or 'your.database.windows.net'
database = 'Filpcart'
username = 'sa'  # Needed for SQL Authentication
password = 'Kanth1186$'  # Needed for SQL Authentication
driver = '{ODBC Driver 17 for SQL Server}'  # Ensure you have the right driver installed

# Create connection function
def sql():
    try:
        conn_str = f"""
            DRIVER={driver};
            SERVER={server};
            DATABASE={database};
            UID={username};
            PWD={password};
            TrustServerCertificate=yes;
        """
        # Establish connection
        conn = pyodbc.connect(conn_str)
        print("Connection successfully")
        return conn
    except pyodbc.Error as e:
        print("Error connecting to SQL Server:", e)
        return None

def pull(query):
    conn = sql()
    if conn is not None:
      try:
          data=pd.read_sql(query,conn)
          print("data pulled")
          return data
      except pyodbc.Error as e:
          print("error",e)
          return None
      finally:
          conn.close()
          print("sql closed")