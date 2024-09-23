import pytest
from perinola import Perinola

def test_prueba():
    assert(True)
def test_constructor():
    p = Perinola()
    assert(p.cara_visible == "Pon 1")
def test_repr():
    p = Perinola()
    msj = p.__repr__()
    assert("Salio: " in msj)
    assert("Pon 1" in msj)
def test_tirar():
    p = Perinola()
    p.tirar()
    
'''    def tirar(self):
        caras = ("Pon 1", "Toma 2", "Todos Ponen",
                "Toma 1", "Pon 2", "Toma Todo")
        self.cara_visible = choice(caras)
        return self.cara_visible
'''        