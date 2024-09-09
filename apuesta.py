class Apuesta:
    def __init__(self,fichas=0):
        if (fichas < 0):
            raise ValueError("La apuesta no puede ser negativa")
        self.fichas = fichas
    def __repr__(self):
        return f"Apuesta: {self.fichas} fichas"
    
    def ponerFicha(self, pone=1):
        self.fichas = self.fichas + pone
    
    def tomarFicha(self, toma=1):
        if toma > self.fichas:
            raise ValueError("No hay tanta cantidad de fichas")
        self.fichas -= toma
    def tomarTodas(self):
        self.fichas = 0
        return self.fichas
    def tieneFicha(self, tiene=1):
        if (self.fichas >= tiene):
            return True
        else: 
            return False
    def estaVacia(self):
        if (self.fichas == 0):
            return True
        else: 
            return False