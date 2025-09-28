#Refactorizar el script de la calculadora lineal en al menos 4 funciones separadas. una por cada tipo de operación. Como ser: Sumar(), Restar(), Multiplicar() y Dividir()

#Añadir manejo de excepciones para entradas inválidas y división por cero.

try:
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))
    operacion = input("Ingrese la operación (+, -, *, /): ")

    # Funciones
    def sumar(a, b):
        return a + b

    def restar(a, b):
        return a - b

    def multiplicar(a, b):
        return a * b

    def dividir(a, b):
        return a / b

    # Validación de operación
    if operacion == "+":
        resultado = sumar(numero1, numero2)
    elif operacion == "-":
        resultado = restar(numero1, numero2)
    elif operacion == "*":
        resultado = multiplicar(numero1, numero2)
    elif operacion == "/":
        resultado = dividir(numero1, numero2)
    else:
        print("Operación inválida. Por favor, ingrese +, -, * o /.")
        resultado = None

    # Imprimir resultado solo si la operación fue válida
    if resultado is not None:
        print(f"El resultado de {numero1} {operacion} {numero2} es: {resultado}")

except ZeroDivisionError:
    print("Error: División por cero no está permitida.")
except ValueError:
    print("Error: Entrada inválida. Por favor ingrese números válidos.")
except Exception as e:
    print(f"Ha ocurrido un error inesperado: {e}")


