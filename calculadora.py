logo = """
 ____________________ |  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

#Suma
def suma(n1, n2):
    return n1 + n2

#Resta
def resta(n1, n2):
    return n1 - n2

#Multiplica
def multiplica(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1/n2

operaciones = {
"+": suma, 
"-": resta, 
"*": multiplica, 
"/": divide
}

def calculadora():
    print (logo)
    num1=float(input("Intro el primer número: "))
   
    for simbolo in operaciones:
        print(simbolo)
    continua = True
    while continua:
        operador=input("Elige + para sumar, - restar, * multiplicar o / para dividir: ")
        num2=float(input("Intro el siguiente número: "))
        funcion_calculo = operaciones[operador]
        resultado=funcion_calculo(num1, num2)
        print(f"{num1}{operador}{num2}  = {resultado}")

        if input("Escribe s para seguir calculando o pulsa t para terminar y comenzar otro calculo: ") == "s":
            num1=resultado
        else:
            continua=False
            calculadora()

calculadora()


