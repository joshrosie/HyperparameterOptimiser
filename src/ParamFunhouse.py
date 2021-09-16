import numpy as np
import matplotlib.pyplot as plt

class ParamFunhouse():

    #parameter pattern:
    #a b c e f r x
    def __init__(self, lowers=None, uppers=None, style='hardcoded'):
        self.parameterSet = [[],
                            [],
                            [],
                            [],
                            [],
                            [],
                            []]

        if lowers is None:     #a #b #c  #e   #f   #r #x
            self.lowerBounds = [1, 1, 10, 0.1, 0.1, 0, 1]
        else:
            self.lowerBounds = lowers

        if uppers is None:      #a   #b    #c     #e  #f    #r   #x
            self.upperBounds = [1000,1000,1000000,1000,1000,100,10000]
        else:
            self.upperBounds = uppers

        #factory-ish
        if style == 'geometric':
            self.defaultGen()
            print(self.parameterSet)

        elif style == 'hardcoded':
            self.hardCodeGen()
        elif style == 'fibonacci':
            self.fibonacciGen()


    def getParameters(self,array): #length of array must = 7
        result = []
        for i in range(7):
            result.append(self.parameterSet[i][array[i]])
        return result

    def defaultGen(self):
        for i in range(7):
            print(np.geomspace(self.lowerBounds[i],self.upperBounds[i],num=20,dtype=int))
            #self.parameterSet[i] = np.geomspace(self.lowerBounds[i],self.upperBounds[i],num=20,dtype=int)
            #plot(i)

    def fibonacciGen(self):
        pass
    
    def hardCodeGen(self):
        self.parameterSet[1] = [1,2,3,4, 5, 6 , 7 ,8, 9 , 10, 15, 20, 30, 50, 100, 200, 300,500,800, 1000]
        self.parameterSet[0] = [1,2,3,4, 5, 6 , 7 ,8, 9 , 10, 15, 20, 30, 50, 100, 200, 300,500,800, 1000]
        self.parameterSet[2] = [10,20,40,80,100,150, 200, 300,400, 500, 800, 1000, 2000, 5000, 8000, 10000, 50000, 100000, 500000, 1000000]
        self.parameterSet[3] = [0.1,0.5,1,4,8,10, 16, 20,40, 80, 120, 300, 400, 500, 600, 700, 800, 900, 950, 1000] 
        self.parameterSet[4] = [0.1,0.2,0.5, 0.8, 1, 2, 3, 4,8,10, 16, 20,40, 80, 120, 300, 500, 700, 900, 1000]   
        self.parameterSet[5] = [0,2,4,6,8,10, 12, 15,20, 25, 30, 35, 40, 45, 50, 60, 70, 80, 90, 100]
        self.parameterSet[6] = [1,2,3,4, 5, 6 , 7 ,8, 9 , 10, 20, 50, 100, 250, 500, 1000, 2000,5000,8000, 10000]


    def plot(self,i):
        x = np.arange(0,20)
        y = self.parameterSet[i]
        plt.plot(x,y)
        plt.show()



