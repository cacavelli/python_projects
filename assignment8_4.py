"""

Este código foi a resposta de uma atividade do curso de Python da Universidade de Michigan.

O arquivo romeo.txt está na pasta para que o código possa ser testado.

Open the file romeo.txt and read it line by line. 
For each line, split the line into a list of words using the split() method. 
The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. 
When the program completes, sort and print the resulting words in alphabetical order.

[Desired output]

['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 
'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 
'window', 'with', 'yonder']

"""

fname = input("Enter file name: ")
fh = open(fname)
romeo = list()

for line in fh:
    line = line.rstrip()
    line = line.split()
    for word in line:
        if word not in romeo: 
            romeo.append(word)

print(sorted(romeo))