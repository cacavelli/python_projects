"""
Este código foi a resposta de uma atividade do curso de Python da Universidade de Michigan.

Exercise 1: Write a program which repeatedly reads numbers until the user enters "done". 
Once "done" is entered, print out the total, count, and average of the numbers. 
If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.


example:
Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.333333333333333
"""

count = 0
tot = 0.0
print("Digite 'done' para encerrar\n")

while True:
    first_data = input("Digite um número: ")
    if first_data == 'done' :
        break
    try:
        num = float(first_data) 
    except:
        print("Entrada inválida")
        continue #faz com que o loop reinicie e vá para a próxima iteração
    count = count + 1 #contador
    tot = tot + num #soma os valores inseridos

print("\nFinito\n")
print("A soma de todos os números é: ", tot)
print("Você digitou um total de ", count, "número(s)")
print("A média dos valores inseridos é: ", tot / count)
