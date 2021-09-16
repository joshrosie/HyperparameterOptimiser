import mysql.connector as mysql

class Repository:
    # Private variables
    __hostName = None
    __userName = None
    __password = None
    __database = None
    __connection = None
    __cursor = None

    # Paramaterised constructor.
    def __init__(self, hostName="localhost", userName ="root", password = "pw", database = "hyperopt"):
        self.__hostName = hostName
        self.__userName = userName
        self.__password = password
        self.__database = database   
 
    def initConnection(self):
        self.__connection = mysql.connect(
            host = self.__hostName,
            user = self.__userName,
            passwd = self.__password,
            database = self.__database
        )
        self.__cursor = self.__connection.cursor()

    def showTables(self):
        self.__cursor.execute("SHOW TABLES")
        tables = self.__cursor.fetchall()
        return tables #must be printed out in for-each loop

    def insert(self,values): #values must be an array?
        # [id,a,b,c,e,f,r,x]
        # may need to validate input?
        # this implementation may be wrong. If so refer to implementation in https://www.datacamp.com/community/tutorials/mysql-python
        query = "INSERT INTO runAncestry (runID, aParam, bParam, cParam, eParam, fParam, rParam, xParam) VALUES({0},{1},{2},{3},{4},{5},{6},{7})"
        id = values[0]
        a = values[1]
        b = values[2]
        c = values[3]
        e = values[4]
        f = values[5]
        r = values[6]
        x = values[7]
        query = query.format(id,a,b,c,e,f,r,x)
        self.__cursor.execute(query) # execute the query
        self.__connection.commit() # commit the update

    def getRun(self, id):
        query = "SELECT * FROM runAncestry WHERE runID = {}".format(id)
        self.__cursor.execute(query)
        run = self.__cursor.fetchall()
        return run # must be accessed in a for-each loop
        


    