# John Rebeles
# PSID: 2039426

user_password = input()

to_replace = {
    'i': '!',
    'a': '@',
    'm': 'M',
    'B': '8',
    'o': '.'
}
new_password = ''

for i in user_password:
    if i in to_replace:
        new_password += to_replace[i]
    else:
        new_password += i

new_password += 'q*s'
print(new_password)
