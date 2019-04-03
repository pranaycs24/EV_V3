class Carconfig:
    def __init__(self,speed, chRate, dchRate):
        self.speed=speed
        self.chRate=chRate
        self.dchRate=dchRate

    def setSpeed(self, speed):
        self.speed=speed

    def setchRate (self, chRate):
        self.chRate=chRate

    def setdchRate(self, dchRate):
        self.dchRate=dchRate

    def getSpeed(self):
        return self.speed

    def getchRate(self):
        return  self.chRate

    def getdchRate(self):
        return self.dchRate