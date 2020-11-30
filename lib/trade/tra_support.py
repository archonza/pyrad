from enum import Enum

class ESupportLevels(Enum):
    S1 = 0
    S2 = 1
    S3 = 2

class Support:
    supportLevels = []

    def calculateSupportLevels(self, pivotPoint, prevHighPrice, prevLowPrice, prevClosePrice):
        self.supportLevels.append((2 * pivotPoint) - prevHighPrice)
        self.supportLevels.append(pivotPoint - (prevHighPrice - prevLowPrice))
        self.supportLevels.append(prevLowPrice - 2 * (prevHighPrice - pivotPoint))

    def getSupportLevel(self, level: ESupportLevels) -> float:
        return self.supportLevels[level.value]