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

    
    def __initConnection(self):
        self.__connection = mysql.connect(
            host = self.__hostName,
            user = self.__userName,
            passwd = self.__password,
            database = self.__database
        )
        self.__cursor = self.__connection.cursor()
        


    