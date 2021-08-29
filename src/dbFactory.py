import mysql.connector as mysql



def dbCreate():
    db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "Joshu@2000"
    )
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE HyperOpt")

def dbCreateTable():
    db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "dbms",
    database = "HyperOpt"
    )
    cursor = db.cursor()
    cursor.execute("CREATE TABLE runAncestry (runID INT NOT NULL AUTO_INCREMENT PRIMARY KEY, )")