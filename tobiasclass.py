class vara:
    def __init__(self, namn, varukod, pris):
        self.namn = namn
        self.varukod = varukod
        self.pris = pris

    def __str__(self):
        return self.namn

    def getvarukod(self):
        return self.varukod

    def getprice(self):
        return f"{self.pris} kr"
