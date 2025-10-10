import random

class Monster():
    def __init__(self, nRows, nCols, maxSpeed):
        self.nRows = nRows
        self.nCols = nCols
        self.maxSpeed = maxSpeed
        self.myRow = random.randrange(self.nRows)
        self.myCol = random.randrange(self.nCols)
        self.mySpeedX = random.randrange(-maxSpeed, maxSpeed + 1)
        self.mySpeedY = random.randrange(-maxSpeed, maxSpeed + 1)

    def move(self):
        self.myRow = (self.myRow + self.mySpeedY) % self.nRows
        self.myCol = (self.myCol + self.mySpeedX) % self.nCols