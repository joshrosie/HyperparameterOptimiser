import mysql.connector as mysql

# Create a database object on the local host. Need to figure out how to make a database on a docker image
def dbCreate():
    db = mysql.connect(
    host = "localhost",
    user = "root",
    password = "supersecret"
    )
    cursor = db.cursor()
    cursor.execute("CREATE DATABASE HyperOpt")

def dbCreateTable():
    db = mysql.connect(
    host = "localhost",
    user = "root",
    password = "???",
    database = "HyperOpt"
    )
    cursor = db.cursor()
    cursor.execute("CREATE TABLE runAncestry (runID INT, aParam INT, bParam INT, cParam INT, eParam INT, fParam INT, rParam INT, xParam INT, evol INT, wcard CHAR(10), obj_val DOUBLE(8,5))")
