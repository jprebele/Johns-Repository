# John Rebeles
# PSID: 2039426

def palindrome_check(u_input):
    u_input = u_input.replace(" ", "")
    if u_input[::-1] == u_input:
        return True
    else:
        return False


user_input = input()
if palindrome_check(user_input):
    print(user_input, "is a palindrome")
else:
    print(user_input, "is not a palindrome")



