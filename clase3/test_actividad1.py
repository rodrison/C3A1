import pytest
from clase3.actividad1 import sumar, restar, multiplicar, dividir

# --- Fixtures ---
@pytest.fixture
def numeros_enteros():
    return 10, 5

@pytest.fixture
def numeros_flotantes():
    return 0.1, 0.2

# --- Tests de Sumar ---
@pytest.mark.smoke
@pytest.mark.parametrize("a, b, resultado", [
    (2, 3, 5),
    (5, 7, 12),
    (-1, 1, 0),
])
def test_sumar(a, b, resultado):
    assert sumar(a, b) == resultado

def test_sumar_enteros(numeros_enteros):
    a, b = numeros_enteros
    assert sumar(a, b) == 15

def test_sumar_flotantes(numeros_flotantes):
    a, b = numeros_flotantes
    assert round(sumar(a, b), 1) == 0.3

# --- Tests de Restar ---
@pytest.mark.parametrize("a, b, resultado", [
    (5, 3, 2),
    (10, 5, 5),
    (-1, -1, 0),
])
def test_restar_param(a, b, resultado):
    assert restar(a, b) == resultado

def test_restar_error():
    with pytest.raises(TypeError):
        restar(10, "a")

# --- Tests de Multiplicar ---
def test_multiplicar():
    assert multiplicar(3, 4) == 12

def test_multiplicar_error():
    with pytest.raises(TypeError):
        multiplicar(2, None)

# --- Tests de Dividir ---
def test_dividir():
    assert dividir(10, 2) == 5

@pytest.mark.exception
def test_dividir_por_cero():
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)
