print("Enter amount of lemon juice (in cups):")
lemon_juice = float(input())
print("Enter amount of water (in cups):")
water = float(input())
print("Enter amount of agave nectar (in cups):")
agave_nectar = float(input())
print("How many servings does this make?")
num_servings = int(input())
print()

print("Lemonade ingredients - yields", '{:.2f}'.format(num_servings), "servings")
print('{:.2f}'.format(lemon_juice), "cup(s) lemon juice")
print('{:.2f}'.format(water), "cup(s) water")
print('{:.2f}'.format(agave_nectar), "cup(s) agave nectar")
print()

print("How many servings would you like to make?")
num_servings2 = float(input())
print()
print("Lemonade ingredients - yields", '{:.2f}'.format(num_servings2), "servings")
lemon_juice = (num_servings2 / num_servings) * lemon_juice
print('{:.2f}'.format(lemon_juice), "cup(s) lemon juice")
water = (num_servings2 / num_servings) * water
print('{:.2f}'.format(water), "cup(s) water")
agave_nectar = (num_servings2 / num_servings) * agave_nectar
print('{:.2f}'.format(agave_nectar), "cup(s) agave nectar")

print()
print("Lemonade ingredients - yields", '{:.2f}'.format(num_servings2), "servings")
lemon_juice = lemon_juice / 16
print('{:.2f}'.format(lemon_juice), "gallon(s) lemon juice")
water = water / 16
print('{:.2f}'.format(water), "gallon(s) water")
agave_nectar = agave_nectar / 16
print('{:.2f}'.format(agave_nectar), "gallon(s) agave nectar")
