# John Rebeles
# PSID: 2039426
from datetime import datetime

user_input = input()
current_date = datetime.now()

while user_input != '-1':
    if user_input.find(','):

        date = datetime.strptime(user_input, '%B %d, %Y')

        if date < current_date:
            date_format = date.strftime('%#m/%#d/%Y')
            print(date_format)
            user_input = input()
    else:
        user_input = input()





