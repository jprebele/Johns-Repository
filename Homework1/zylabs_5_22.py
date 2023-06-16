# John Rebeles
# PSID:2039426

print("Davy\'s auto shop services\nOil change -- $35\nTire rotation -- $19\nCar wash -- $7\nCar wax -- $12")
print()

d_services = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12, '-': 'No service'}

first_service = input("Select first service:\n")
second_service = input("Select second service:\n")
print()

print("Davy's auto shop invoice\n")
if first_service == '-':
    print(f'Service 1: {d_services[first_service]}')
else:
    print('Service 1: ' + first_service + ',', end=' ')
    print(f'${d_services[first_service]}')

if second_service == '-':
    print(f'Service 2: {d_services[second_service]}\n')
else:
    print('Service 2: ' + second_service + ',', end=' ')
    print(f'${d_services[second_service]}\n')

if first_service == '-':
    d_services['-'] = 0
elif second_service == '-':
    d_services['-'] = 0

first_service = int(d_services.get(first_service))
second_service = int(d_services.get(second_service))
sum_ser = str(first_service + second_service)
print('Total: $' + sum_ser)
