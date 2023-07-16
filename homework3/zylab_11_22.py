# John Rebeles
# PSID: 209426

user_input = input().split()

counter = {}

for word_input in user_input:
    if word_input in counter:
        counter[word_input] += 1
    else:
        counter[word_input] = 1

for words in user_input:
    print(f'{words} {counter[words]}')
