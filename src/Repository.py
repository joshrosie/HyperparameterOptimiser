import mysql.connector as mysql

class Repository:
    # Private variables
    __hostName = None
    __userName = None
    __password = None
    __database = None
    __connection = None
    __cursor = None

# Test
# Constructor:
#   Test that the object constructed is the one you tried to construct
# initConnection:
#   Can maybe validate by using the cursor to pull something we know is in the 
#   database.
# insert:
#   Can get number of rows in table before and after method call
# getRun:
#   Can use a toy run as proof of concpet

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
        query = "INSERT INTO runAncestry (aParam, bParam, cParam, eParam, fParam, rParam, xParam, P1, P2, P3, Score,stateFile) VALUES({}.{},{},{},{},{},{},{},{},{},{},{})"
        a = values[0]
        b = values[1]
        c = values[2]
        e = values[3]
        f = values[4]
        r = values[5]
        x = values[6]
        p1 = values[7]
        p2 = values[8]
        p3 = values[9]
        score = values[10] #where tf do we determine score? what is score? pain
        stateFile = values[11]
        query = query.format(a,b,c,e,f,r,x,p1,p2,p3,score,stateFile)
        self.__cursor.execute(query) # execute the query
        self.__connection.commit() # commit the update

    def getRun(self, id):
        query = "SELECT * FROM runAncestry WHERE runID = {}".format(id)
        self.__cursor.execute(query)
        run = self.__cursor.fetchall()
        return run # must be accessed in a for-each/range based for loop
        
    def getRunRange(self, loBound, upBound):
        query = "SELECT * FROM runAncestry WHERE runID BETWEEN {} AND {}".format(loBound,upBound)
        self.__cursor.execute(query)
        runs = self.__cursor.fetchall()
        return runs


    def getStatesRanked(self,x):
        GA_P1 = x[7]
        GA_P2 = x[8]
        GA_P3 = x[9]
        #query = "SELECT stateFile, (  min(   (p1 - {})^2)  +  (p2 - {})^2  +  ((p3 - {})^2)*0.5) )  ) as Score FROM runAncestry ORDER BY Score".format(GA_P1,GA_P2,GA_P3)
        # if we store score in runAncestry and input it when we get p1 p2 p3:
        query = "SELECT TOP 1 FROM runAncestry ORDER BY ((P1 - {})^2)  +  (P2 - {})^2  +  ((P3 - {})^2)*0.5))".format(GA_P1,GA_P2,GA_P3)
        self.__cursor.execute(query)
        run = self.__cursor.fetchall()
        return run



    