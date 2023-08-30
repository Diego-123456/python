class CLArray2:
    
    n = 100
    
    def __init__(self):
        self.__nom = [0]*self.n
        self.__edad = [0]*self.n
        self.__i=0
        
    def getCargar(self, Nom, Edad):
        self.__nom[self.__i] = Nom
        self.__edad[self.__i] = Edad
        self.__i+= 1
    
    def getMostrar(self):
        r = ""
        for c in range(0,self.__i):
            r += self.__nom[c] +" "+ str(self.__edad[c])+"\n"
        return r
        
    