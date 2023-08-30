class CLCarrera:

    def __init__(self):
        self.__pre=0
        self.mat=0
        self.__lib=0
        self.__car=0

    def getArray(self):
        car = ["Ing. Sistema","Ing. Industrial","Ing. Mecanica"]
        return car 

    def getPre(self,pos):
        pre = [650, 790, 780]
        self.__pre = pre[pos]
        return self.__pre

    def getTo(self):
        return self.__pre+self.mat

    def getLib(self, tipo):
        if tipo==0: self.__lib=0
        elif tipo==1: self.__lib=60
    
    def getCar(self, tipo):
        if tipo==0: self.__car=0
        elif tipo==1: self.__car=120
    
    def getNeto(self):
        return self.getTo()+self.__lib+self.__car
