    
from apuesta import Apuesta
from perinola import Perinola


p = Perinola()
print(p)
resultado = p.tirar()
print(resultado)

a = Apuesta()
print(a)
a.ponerFicha(4)
print(a)
a.ponerFicha()
print(a)
a.tomarFicha()
print(a)
a.tomarFicha(1)
print(a)

