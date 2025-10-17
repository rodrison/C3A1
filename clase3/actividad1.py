# funciones de la calculadora
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("División por cero no permitida")
    return a / b

# código interactivo SOLO se ejecuta si corres el archivo directamente
if __name__ == "__main__":
    try:
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))
        operacion = input("Ingrese la operación (+, -, *, /): ")

        if operacion == "+":
            resultado = sumar(numero1, numero2)
        elif operacion == "-":
            resultado = restar(numero1, numero2)
        elif operacion == "*":
            resultado = multiplicar(numero1, numero2)
        elif operacion == "/":
            resultado = dividir(numero1, numero2)
        else:
            print("Operación inválida")
            resultado = None

        if resultado is not None:
            print(f"El resultado de {numero1} {operacion} {numero2} es: {resultado}")

    except Exception as e:
        print(f"Ha ocurrido un error inesperado: {e}")
