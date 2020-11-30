class PivotPoint:
    value = 0.0

    def getValue(self) -> float:
        return self.value

    def calculatePivotPoint(self, prevHighPrice, prevLowPrice, prevClosePrice):
        self.pivotPoint = ((prevHighPrice + prevLowPrice + prevClosePrice) / 3)