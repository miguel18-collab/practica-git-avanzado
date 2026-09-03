# Calculadora - Funciones adicionales

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero"
    return a / b

def potencia(base, exponente):
    return base ** exponente

def raiz_cuadrada(numero):
    if numero < 0:
        return "Error: no existe raiz de un numero negativo"
    return numero ** 0.5

def porcentaje(numero, porcentaje):
    return numero * (porcentaje / 100)

def promedio(lista_numeros):
    return sum(lista_numeros) / len(lista_numeros)

# Nueva funcionalidad: factorial
def factorial(n):
    """Calcula el factorial de un número entero no negativo."""
    if n < 0:
        return "Error: no existe factorial de negativo"
    if n == 0:
        return 1
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado