import mysql.connector as mysql
# We attempted to make this class a singleton. However, we soon found that this is more complicated to implement in python as the
# constructor does not work in the same way as more object oriented languages like Java. The idea behind making this class a singleton
# is that we want a hard restriction on the number of repositories that can exist which should only ever been one. Further exploration
# revealed that while it is possible to turn a python class into a singleton, it is an arduous process. It will be something that we will
# look into implementing if we have time after we meet the minimal requirements.
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
        query = "INSERT INTO runAncestry (Session, Generation, PopulationMember, aParam, bParam, cParam, dParam,eParam, fParam, rParam, xParam, Timeout, zParam, iParam, wParam, EndScore, StartScore, StartTime, EndTime, P1, P2, P3) VALUES({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})"
        s = values[0] #keep track of session number to discern which files are valid input files
        g = values[1] # not sure
        p = values[2] # not sure       
        a = values[3] # standard params
        b = values[4]
        c = values[5]
        d = values[6] 
        e = values[7]
        f = values[8]
        r = values[9]
        x = values[10]
        timeout = values[11] 
        z = values[12]
        i = values[13]
        w = values[14]
        endscore = values[15]   #used for LSD
        startscore = values[16]
        starttime = values[17]
        endtime = values[18]
        p1 = values[19]
        p2 = values[20]
        p3 = values[21]
      
        query = query.format(s,g,p,a,b,c,d,e,f,r,x,timeout,z,i,w,endscore,startscore,starttime,endtime,p1,p2,p3)
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

    # orders db in terms of score (descending) then selects every state file from the current session
    def getStatesRanked(self,pymooParams, sessionNumber): #required to do: need to figure out a way to keep track of session
        #P1 = EndScore [15]
        #P2 = StartScore [16] - EndScore [15]
        #P3 = StartTime [17] - EndTime [18]
        
        GA_P1 = pymooParams[15]
        GA_P2 = pymooParams[16] - pymooParams[15]
        GA_P3 = pymooParams[17] - pymooParams[18]
        query = "SELECT iParam FROM runAncestry WHERE Session = {} ORDER BY ((P1 - {})^2  +  (P2 - {})^2  +  ((P3 - {})^2)*0.5)".format(sessionNumber,GA_P1,GA_P2,GA_P3)
        self.__cursor.execute(query)
        stateFiles = self.__cursor.fetchall()
        return stateFiles

#is iParam right?

    
