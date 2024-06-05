# Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação e 
# o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
# 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão
# Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

import os
def inicio():
    print ('\n------ CALCULADORA ------')
    operacao = input('''# 1. Soma
# 2. Subtração
# 3. Multiplicação
# 4. Divisão
DIGITE O NUMERO DA OPERAÇÃO:''')
    if operacao== '1':
        soma()
    elif operacao == '2':
        subtracao()
    elif operacao == '3':
        multiplica()
    elif operacao == '4':
        divide()
    else:
        print('\n!!!!!!!operação invalida!!!!!!\n')
        inicio()  

def bugdivisao():
    print('\n!!! O NUMERO NÃO PODE SER DIVIDIDO POR ZERO !!!\n')
    divide()

def soma():
    num1 = float(input('\nDIGITE O PRIMEIRO NUMERO: '))
    num2 = float(input('\nDIGITE O SEGUNDO NUMERO: '))
    resultado = num1+num2
    print('\nO RESULDADO DA SOMA É: ',resultado)
    operacao()

def subtracao():
    num1 = float(input('\nDIGITE O PRIMEIRO NUMERO: '))
    num2 = float(input('\nDIGITE O SEGUNDO NUMERO: '))
    resultado = num1-num2
    print('\nO RESULDADO DA SUBTRAÇÃO É: ',resultado)
    operacao()

def multiplica():
    num1 = float(input('\nDIGITE O PRIMEIRO NUMERO: '))
    num2 = float(input('\nDIGITE O SEGUNDO NUMERO: '))
    resultado = num1*num2
    print('\nO RESULDADO DA MULTIPLICAÇÃO É: ',resultado)
    operacao()

def divide():
    num1 = float(input('\nDIGITE O PRIMEIRO NUMERO: '))
    num2 = float(input('\nDIGITE O SEGUNDO NUMERO: '))
    if num2 ==0:
        bugdivisao()

    else:
        resultado = num1/num2
        print(f'\nO RESULDADO DA DIVISÃO É: ',resultado)
        operacao()

def operacao():
    operacao= input('\nPARA FAZER OUTRA OPERAÇÃO DIGITE 1: ')
    if operacao == '1':
        inicio()
    else:
        os.system('cls')

inicio() 

