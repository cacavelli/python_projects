"""

Este código foi a resposta de uma atividade do curso de Python da Universidade de Michigan.

O arquivo words.txt está na pasta para que o código possa ser testado.

Exercise 7.1 
Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. 
Use the file words.txt to produce the output below.
"""


# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.rstrip() #remove os whitespaces do final. 

    print(line.upper())