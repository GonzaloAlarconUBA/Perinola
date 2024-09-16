class Jugador:
    def __init__(self, nombre, fichas= 5):
        self.nombre = nombre
        self.fichas = fichas
    def __repr__(self):
        return f"{self.nombre}, {self.fichas} fichas"
    def darFicha(self, fichas):
        self.fichas = self.fichas + fichas
    def tomarFicha(self, fichas=1):
        if fichas > self.fichas:
            raise ValueError("No hay tanta cantidad de fichas")
        self.fichas -= fichas
    def tomarTodas(self):
        self.fichas = 0
        return self.fichas
    def tieneFicha(self, fichas=1):
        return self.fichas >= fichas
    def estaVacia(self):
        return self.fichas == 0
