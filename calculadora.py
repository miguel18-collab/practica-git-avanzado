# Calculadora

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

def potencia(a, b):
    return a ** b

def menu():
    print("Bienvenido a la calculadora mas genial del mundo")
    print("Opciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    
    while True:
        opcion = input("Seleccione una opción (1/2/3/4/5): ")
        
        if opcion in ["1", "2", "3", "4", "5"]:
            try:
                a = float(input("Ingrese el primer número: "))
                b = float(input("Ingrese el segundo número: "))
            except ValueError:
                print("Error: Ingrese números válidos")
                continue
            
            if opcion == "1":
                resultado = sumar(a, b)
                print(f"El resultado de la suma es: {resultado}")
            elif opcion == "2":
                resultado = restar(a, b)
                print(f"El resultado de la resta es: {resultado}")
            elif opcion == "3":
                resultado = multiplicar(a, b)
                print(f"El resultado de la multiplicación es: {resultado}")
            elif opcion == "4":
                resultado = dividir(a, b)
                print(f"El resultado de la división es: {resultado}")
            elif opcion == "5":
                resultado = potencia(a, b)
                print(f"El resultado de la potencia es: {resultado}")
            break
        else:
            print("Opción no válida. Por favor, seleccione 1, 2, 3, 4 o 5.")

if __name__ == "__main__":
    menu()


