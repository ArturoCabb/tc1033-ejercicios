#-*- coding: utf-8 -*-

def greet(value1, value2):
    print("Hello ", value1 + " " + value2)

def run(a, b, c, d, e):
    if numero >= 0 and numero <=10:
        x = 0
        while x < numero:
            print("Running")
            x = x + 1

def perceptron(a, b, c, d):
    if (a*b + c*d) > 20:
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    Hansel = str(input("Ingresa tu nombre: "))
    Gretel = str(input("Ingresa tus Apellidos: "))
    greet(Hansel, Gretel)
    
    num1 = int(input("Ingrese un número del 0 al 10: "))
    num2 = int(input("Ingrese un número del 0 al 10: "))
    num3 = int(input("Ingrese un número del 0 al 10: "))
    num4 = int(input("Ingrese un número del 0 al 10: "))
    num5 = int(input("Ingrese un número del 0 al 10: "))
    run(num1, num2, num3, num4, num5)

    perceptron(1, 5, 1, 5)
    perceptron(1, 10, 1, 5)
    perceptron(1, 5, 1, 10)