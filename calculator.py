# Calculadora em Python
'''A ideia é ter uma calculadora básica que realize:

1 - Soma;
2 - Subtração;
3 - Multiplicação;
4 - Divisão;
5 - Potência

O usuário seleciona o que deseja fazer digitando a opção e depois os dois números para realizar a operação matemática.

Caso digite algo fora das 5 opções, a calculadora informa <Opção inválida>'''

#CRIAR OUTRO PROGRAMA PARA CONVERSÕES 

#CRIAR OUTRO PROGRAMA PARA CALCULOS GEOMÉTRICOS

#variáveis inseridas pelo usuário para realizar a operação
num1 = 0
num2 = 0

#lista de opções
opcoes = ['1 - Soma', '2 - Subtração', '3 - Multiplicação', '4 - Divisão', '5 - Potência']

#slice de lista
op1 = opcoes[0]
op2 = opcoes[1]
op3 = opcoes[2]
op4 = opcoes[3]
op5 = opcoes[4]

#Definição de funções de Adição, Subtração, Divisão, Resto de divisao, MATEMÁTICASultiplicação e Potência
def soma (num1, num2):
    return num1 + num2

def subtracao (num1, num2):
    return num1 - num2


def divisao (num1, num2):
    return num1 / num2

def resto (num1, num2):
    return num1 % num2

def multiplicacao (num1, num2):
    return num1 * num2

def potencia (num1, num2):
    return num1 ** num2


#Imprime na tela a lista de opções do usuário e pede para que ele escolha a operação matemática que deseja realizar
print("******************PYTHON CALCULATOR******************\n")
print()
print(op1)
print(op2)
print(op3)
print(op4)
print(op5)
opcoesSeleciona = int(input("\nDigite a opção desejada: "))

if opcoesSeleciona >= 6:
#Mensagem de erro em caso de opção inválida
    print("\n****Opção Inválida!****")

elif opcoesSeleciona == 1:
#Soma dos números informados pelo usuário
    print("\nSOMA SELECIONADA.")
    num1 = int(input("\nDigite um número: "))
    num2 = int(input("Digite mais um número: "))
    print("\nO resultado da soma dos valores informados é: ", soma(num1, num2))

elif opcoesSeleciona == 2:
#Subtração dos números informados pelo usuário
    print("\nSUBTRAÇÃO SELECIONADA.")
    num1 = int(input("\nDigite um número: "))
    num2 = int(input("Digite mais um número: "))
    print("\nO resultado da subtração dos valores informados é: ", subtracao(num1, num2))

elif opcoesSeleciona == 3:
#Multiplicação dos números informados pelo usuário
    print("\nMULTIPLICAÇÃO SELECIONADA.")
    num1 = int(input("\nDigite um número: "))
    num2 = int(input("Digite mais um número: "))
    print("\nO resultado da multiplicação dos valores informados é: ", multiplicacao(num1, num2))

elif opcoesSeleciona == 4:
#Divisão dos números informados pelo usuário
    print("\nDIVISÃO SELECIONADA")
    num1 = float(input("\nDigite um número: "))
    num2 = float(input("Digite mais um número: "))
    try:
        print("\nO resultado da divisão dos valores informados é: ", divisao(num1, num2), "\nO resto da divisão dos valores informados é: ", resto(num1,num2))
    except:
        print("\nOperação inválida.")

elif opcoesSeleciona == 5:
#Cálculo da potência do primeiro número elevado ao segundo número informado pelo user.
    print('\nPOTÊNCIA SELECIONADA.')
    num1 = int(input("\nDigite um número: "))
    num2 = int(input("Digite mais um número: "))   
    print("\nO resultado de ", num1, " elevado a ", num2, " é igual a: ", potencia(num1, num2))

#Agradecimento e finalização do programa.
print("\nObrigado por ter usado minha calculadora.")
