from enum import Enum

class EResistanceLevels(Enum):
    R1 = 0
    R2 = 1
    R3 = 2

class Resistance:
    resistanceLevels = []

    def calculateResistanceLevels(self, pivotPoint, prevHighPrice, prevLowPrice, prevClosePrice):
        self.resistanceLevels.append((2 * pivotPoint) - prevLowPrice)
        self.resistanceLevels.append(pivotPoint + (prevHighPrice - prevLowPrice))
        self.resistanceLevels.append(prevHighPrice + 2 * (pivotPoint - prevLowPrice))

    def getResistanceLevel(self, pivotPoint, level: EResistanceLevels) -> float:
        return self.resistanceLevels[level.value]