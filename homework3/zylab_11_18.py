# John Rebeles
# PSID: 209426

numbers = [int(i) for i in input().split()]

only_positive = []
for i in numbers:
    if i >= 0:
        only_positive.append(i)

print(*sorted(only_positive), end=' ')

