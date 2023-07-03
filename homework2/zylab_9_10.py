# John Rebeles
# PSID: 2039426
import csv

input_file = input()
with open(input_file, 'r') as csvfile:
    words = csv.reader(csvfile, delimiter=',')

    number_of_words = {}

    for i in words:
        for j in i:
            if j not in number_of_words:
                number_of_words[j] = 1
            else:
                number_of_words[j] += 1

    for j, num in number_of_words.items():
        print(f'{j} {num}')
