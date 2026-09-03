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