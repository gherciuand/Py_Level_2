import pyodbc
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=TO_DO;UID=postgres;PWD=123')
#cnxn = pyodbc.connect('DRIVER={CData ODBC Driver for PostgreSQL};User=postgres;Password=123;Database=postgres;Server=127.0.0.1')