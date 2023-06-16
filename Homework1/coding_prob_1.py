# John Rebeles
# PSID:2039426

print('Birthday Calculator\nCurrent day')
current_month = int(input("Month: "))
current_day = int(input("Day: "))
current_year = int(input("Year: "))
print("Birthday")
bd_month = int(input("Month: "))
bd_day = int(input("Day: "))
bd_year = int(input("Year: "))

if (current_month and current_day) == (bd_month and bd_day):
    print("Happy Birthday!")

print("You are " + str(current_year - bd_year) + " years old.")
