"""

Este código foi a resposta de uma atividade do curso de Python da Universidade de Michigan.

O arquivo mbox-short.txt está na pasta para que o código possa ser testado.


Exercise 7.2 
Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
X-DSPAM-Confidence:    0.8475
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. 
Do not use the sum() function or a variable named sum in your solution.

RESULTADO DESEJADO:

Average spam confidence: 0.750718518519

"""

fname = input("Enter file name: ")
fh = open(fname)
count = 0
average = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    line = line.rstrip()
    fspam = line.find(" ")
    count = count + 1
    final_spam = line[fspam:]
    final_spam = float(final_spam)
    average = average + final_spam
    #print(line)
    
print("Average spam confidence:", average / count)