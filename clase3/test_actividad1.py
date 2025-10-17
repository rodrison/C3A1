import pytest
from clase3.actividad1 import sumar, restar, multiplicar, dividir

@pytest.mark.basic
@pytest.mark.parametrize("a, b, resultado", [
    (2, 3, 5),
    (5, 7, 12),
    (-1, 1, 0),
    (0, 0, 0)
])    

def test_sumar(a,b,resultado):
    assert sumar(a, b) == resultado

#def test_restar():
#    assert restar(5, 2) == 3

#def test_multiplicar():
#    assert multiplicar(3, 4) == 12

#def test_dividir():
#    assert dividir(10, 2) == 5


@pytest.mark.errors
def test_dividir_por_cero():
    with pytest.raises(ZeroDivisionError):
       dividir(10, 0)

@pytest.mark.skip(reason="Test deshabilitado temporalmente")
def test_restar():
    assert restar(5, 2) == 3