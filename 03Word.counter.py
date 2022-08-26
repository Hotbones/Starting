#Contador de palabras

# Pregunta: ¿En qué estás pensando?
# Entrada: Bien, hoy es el día en el que me voy a crear un desarrollador experto
# Salida: ¡Muy bien, tu me has mostrado tu pensamiento en 15 palabras!

import csv
import string

print('The words in the text are: ')
translator = str.maketrans('', '', string.punctuation)

word_count = {}
text = open('declaration.txt').read()

words = text.split()
for word in words:
    word = word.translate(translator).lower()
    count = word_count.get(word, 0)
    count += 1
    word_count[word] = count

word_count_list = sorted(word_count, key=word_count.get, reverse=True)
for word in word_count_list[:10]:
    
    print(word, word_count[word])

# output_file = open('words.csv', 'w') #crea un archivo
# writer = csv.writer(output_file)
# writer.writerow(['word', 'count'])
# for word in word_count_list:
#    writer.writerow([word, word_count[word]])