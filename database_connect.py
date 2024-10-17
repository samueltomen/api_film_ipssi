# Fichier de connexion à la base de données SQL Server
import pyodbc


def connect_db():
    server = "GRAM\\SQLEXPRESS"
    database = "movies_db"

    conn_str = f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;"

    try:
        connection = pyodbc.connect(conn_str)
        print("Connexion réussie à la base de données SQL Server.")
        return connection

    except pyodbc.Error as e:
        print(f"Erreur lors de la connexion : {e}")
        return None
