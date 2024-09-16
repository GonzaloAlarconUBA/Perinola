import pytest
from jugador import Jugador

def test_prueba():
    assert(True)
def test_constructor():
    j = Jugador("Julian")
    assert(j.fichas == 5)
    assert(j.nombre == "Julian")
def test_repr():
    j = Jugador("Julian")
    j.fichas = 4
    msj = j.__repr__()
    assert("Julian" in msj)
    assert("fichas" in msj)
    assert("4" in msj)
def test_tomarFicha():
    j = Jugador("Julian")
    j.tomarFicha(2)
    assert(j.fichas == 3)
def test_tomarFicha_SinArgumento():
    j = Jugador("Julian")
    j.tomarFicha()
    assert(j.fichas == 4)
def test_tomarVarias():
    j = Jugador("Julian")
    j.tomarFicha(2)
    j.tomarFicha(3)
    assert(j.fichas == 0)
def test_tomarFicha_error():
    with pytest.raises(ValueError):
        j = Jugador("Julian")
        j.fichas = 5
        j.tomarFicha(6)
    j = Jugador("Julian")
    j.tomarFicha(5)
    assert(j.tomarFicha)