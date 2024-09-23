from jugador import Jugador

class Ronda: 
    def __init__(self):
        self.jugadores = []
    def __repr__(self):
        s = ""
        for j in self.jugadores:
            str(j) + "\n"
        return s

    def agregarJugador(self):
        self.jugadores.append(Jugador)
    
    def sacarJugadoresSinFichas(self):
        a_sacar = []
        for i in range(0, len(self.jugadores)):
            if self.jugadores[i] == 0:
                a_sacar.append(i)
        for i in reversed(a_sacar):
            self.jugadores.pop(i)
            n = self.jugadores.pop(i)
            print(f"Perdió {n}")


    def jugadorEnTurno(self):
        return(f"Le toca a {self.jugadores[0]}")

    def pasarTurno(self):
        f = Jugador.fichas.pop(0)
        Jugador.fichas.append(f)
        n = Jugador.nombre.nombre.pop(0)
        Jugador.nombre.append(n)

    def quedaSoloUnJugador(self):
        if len(self.jugadores) < 1:
            return True 
        else: 
            return False