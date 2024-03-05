class Calculadora:
    def __init__(self):
        self.num1 = None
        self.num2 = None

    def operando1(self):
        self.num1 = float(input("Introduzca el primer operando: "))

    def operando2(self):
        self.num2 = float(input("Introduzca el segundo operando: "))

    def sumar(self):
        return self.num1 + self.num2

    def restar(self):
        return self.num1 - self.num2

    def multiplicar(self):
        return self.num1 * self.num2

    def dividir(self):
        if self.num2 == 0:
            return "División por cero no permitida"
        return self.num1 / self.num2

    def mostrar_menu(self):
        print("-" * 20)
        print("CALCULADORA")
        print("-" * 20)
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. salir")
        print("-" * 20)

    def elegir_operacion(self):
        opcion = int(input("Elige una opción: "))
        while opcion < 1 or opcion > 5:
            opcion = int(input("Opción no válida. Elige una opción: "))
        return opcion

# Ejemplo de uso
calculadora = Calculadora()

while True:
    calculadora.mostrar_menu()
    opcion = calculadora.elegir_operacion()

    if opcion == 1:
        calculadora.operando1()
        calculadora.operando2()
        print("-----------------------------------------")
        print(f"Suma: {calculadora.sumar()}")
        print("------------------------------------------")
    elif opcion == 2:
        calculadora.operando1()
        calculadora.operando2()
        print("------------------------------------------")
        print(f"Resta: {calculadora.restar()}")
        print("-------------------------------------------")
    elif opcion == 3:
        calculadora.operando1()
        calculadora.operando2()
        print("----------------------------------------------")
        print(f"Multiplicación: {calculadora.multiplicar()}")
        print("-----------------------------------------------")
    elif opcion == 4:
        calculadora.operando1()
        calculadora.operando2()
        print("-------------------------------------------------")
        print(f"División: {calculadora.dividir()}")
        print("--------------------------------------------------")
    elif opcion ==5:
        exit()

