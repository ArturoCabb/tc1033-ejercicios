#-*- coding: utf-8 -*-

def greet(value1):
    print("Hello ", value1)

def run(numero):
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
    name = str(input("Ingresa tu nombre: "))
    greet(name)
    
    num1 = int(input("Ingrese un número del 0 al 10: "))
    run(num1)

    num1 = int(input("Ingrese un número"))
    mum2 = int(input("Ingrese un número"))
    num3 = int(input("Ingrese un número"))
    num4 = int(input("Ingrese un número"))
    perceptron(num1, num2, num3, num4)