# John Rebeles
# PSID: 2039426
def exact_change(user_total):
    dollars = user_total // 100
    cents = user_total % 100

    quarters = cents // 25
    cents = cents % 25

    dimes = cents // 10
    cents = cents % 10

    nickels = cents // 5
    cents = cents % 5

    return dollars, quarters, dimes, nickels, cents


if __name__ == '__main__':
    input_val = int(input())

    if input_val == 0:
        print("no change")
        exit()
    else:
        num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

        if num_dollars > 0:
            if num_dollars == 1:
                print(num_dollars, "dollar")
            else:
                print(num_dollars, "dollars")

        if num_quarters > 0:
            if num_quarters == 1:
                print(num_quarters, "quarter")
            else:
                print(num_quarters, "quarters")

        if num_dimes > 0:
            if num_dimes == 1:
                print(num_dimes, "dime")
            else:
                print(num_dimes, "dimes")

        if num_nickels > 0:
            if num_nickels == 1:
                print(num_nickels, "nickel")
            else:
                print(num_nickels, "nickels")

        if num_pennies > 0:
            if num_pennies == 1:
                print(num_pennies, "penny")
            else:
                print(num_nickels, "pennies")
