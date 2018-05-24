import numpy as np

class Circle:

    def __init__(self,xLoc=0,yLoc=0):
        self.radius = np.random.randint(1,12)
        self.thickness = np.random.randint(0,self.radius)
        self.color = self.getRandomColor()
        self.Location = [xLoc,yLoc]
        self.GrowSpeed = np.random.randint(1,8)

    def UpdateSize(self):
        self.radius +=self.GrowSpeed

    def getRandomColor(self):
        return (np.random.randint(0,255),np.random.randint(0,255),np.random.randint(0,255))
