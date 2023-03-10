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
    __sessionNumber = None

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
        self.deriveSessionNumber()

    def showTables(self):
        self.__cursor.execute("SHOW TABLES")
        tables = self.__cursor.fetchall()
        return tables #must be printed out in for-each loop

    def insert(self,values): #values must be an array?
        # [id,a,b,c,e,f,r,x]
        # may need to validate input?
        # this implementation may be wrong. If so refer to implementation in https://www.datacamp.com/community/tutorials/mysql-python
        query = "INSERT INTO runAncestry (SessionID, Generation, PopulationMember, aParam, bParam, cParam, dParam,eParam, fParam, rParam, xParam, timeoutMs, zParam, iParam, wParam, EndScore, StartScore, StartTime, EndTime, P1, P2, P3) VALUES({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})"
       # s = values[0] #keep track of session number to discern which files are valid input files
        
        g = values[0] # not sure
        p = values[1] # not sure       
        a = values[2] # standard params
        b = values[3]
        c = values[4]
        d = values[5] 
        e = values[6]
        f = values[7]
        r = values[8]
        x = values[9]
        timeout = values[10] 
        z = values[11]
        i = values[12]
        w = values[13]
        endscore = values[14]   #used for LSD # A #P1
        startscore = values[15] #B
        starttime = values[16] #C
        endtime = values[17] #D
       # improvement = values[19] #E
      #  stucktime = values[20] #F
        p1 = values[18]
        p2 = values[19]
        p3 = values[20]
      
        query = query.format(self.__sessionNumber,g,p,a,b,c,d,e,f,r,x,timeout,z,i,w,endscore,startscore,starttime,endtime,p1,p2,p3)
        self.__cursor.execute(query) # execute the query
        self.__connection.commit() # commit the update
    
    def deriveSessionNumber(self):
        query = "SELECT SessionID FROM runAncestry ORDER BY SessionID DESC LIMIT 1;"
        self.__cursor.execute(query)
        self.__sessionNumber = self.__cursor.fetchall()[0][0] + 1
        
        


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
    def getStatesRanked(self,pymooParams): #required to do: need to figure out a way to keep track of session
        #P1 = EndScore [15]
        #P2 = StartScore [16] - EndScore [15]
        #P3 = StartTime [17] - EndTime [18]
        
        #Kiera: pymooparams = p1 p2 p3
        GA_P1 = pymooParams[0] #p1 = A #endscore
        GA_P2 = pymooParams[1] #p2 = E #improvement
        GA_P3 = pymooParams[2] #p3 = F #stucktime
        
        # GA_P1 = pymooParams[15] # is p123 actuall parameters that pymoo optimises? #kiera: yeah
        # GA_P2 = pymooParams[16] - pymooParams[15]
        # GA_P3 = pymooParams[17] - pymooParams[18]
        
            #select statefileName (output file that had those results saved, might be -w param) order by (GA_P1 - EndScore)^2 + (GA_P2 - (EndScore - startScore )^2 + one for P3 etc.)
        query = "SELECT iParam FROM runAncestry WHERE SessionID = {} ORDER BY ((P1 - {})^2  +  (P2 - {})^2  +  ((P3 - {})^2)*0.5)".format(self.__sessionNumber,GA_P1,GA_P2,GA_P3)
        self.__cursor.execute(query)
        stateFiles = self.__cursor.fetchall()
        return stateFiles

 #needed to keep pymoo's parameters up to date
    def getMin(p): 
        pass
        #given p eg. 'a' find the min a for this session return a int/float/value
        
    def getMax(p):
        #given p eg. 'a' find the max a for this session
        pass
#is iParam right?

#confirm input
