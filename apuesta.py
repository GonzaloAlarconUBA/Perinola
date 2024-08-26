class Apuesta:
    def __init__(self,fichas=0):
        if (fichas < 0):
            raise ValueError("La apuesta no puede ser negativa")
        self.fichas = fichas
    def __repr__(self):
        return f"Apuesta: {self.fichas}"
    def ponerFicha(self, pone=1):
        self.pone = pone
        suma = self.fichas + self.pone
        return suma
    def tomarFicha(self, toma=1):
        self.toma = toma
        resta = self.fichas - self.toma
        return resta
    
a = Apuesta()
resultado = a.tomarFicha()
print(resultado)