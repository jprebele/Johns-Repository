# John Rebeles
# PSID: 2039426
import csv
import datetime


class InventoryItems:
    def __init__(self, item_id='N/A', man_name='N/A', item_type='N/A', damage_indicator=False, price=0,
                 service_date='none'):
        self.item_id = item_id
        self.man_name = man_name
        self.item_type = item_type
        self.damage_indicator = damage_indicator
        self.price = price
        self.service_date = service_date


def csv_reader(csv_file, index):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        extracted_data = {}
        for row in reader:
            extracted_data[row[index]] = row
    return extracted_data


# Function to convert the date string to a date object
def convert_to_date(u_date):
    if u_date == 'none':
        return 'none'
    else:
        return datetime.datetime.strptime(u_date, '%m/%d/%Y').date()


# putting data from csv files into variables
manufacturer_data = csv_reader('ManufacturerList.csv', 0)
price_data = csv_reader('PriceList.csv', 0)
service_data = csv_reader('ServiceDatesList.csv', 0)

# create inventory objects with their values and store them in the full_inventory list
full_inventory_list = []

for item_id, data in manufacturer_data.items():
    manufacturer_name, inventory_type, damage_indicator = data[:3]
    price = int(price_data.get(item_id, [0, 0])[1])
    serv_date = service_data.get(item_id, [0, 'none'])[1]
    service_date = convert_to_date(serv_date)
    inventory_item = InventoryItems(item_id, manufacturer_name, inventory_type, damage_indicator, price, service_date)
    full_inventory_list.append(inventory_item)

# Sort the full inventory list by manufacturer name (using selection sort)
for i in range(len(full_inventory_list)):
    index = i
    for j in range(i + 1, len(full_inventory_list)):
        if full_inventory_list[j].man_name < full_inventory_list[index].man_name:
            index = j
    full_inventory_list[i], full_inventory_list[index] = full_inventory_list[index], full_inventory_list[i]

# Output the FullInventory.csv
with open('FullInventory.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Item ID', 'Manufacturer', 'Item Type', 'Price', 'Service Date', 'Damaged'])

    for item in full_inventory_list:
        writer.writerow(
            [item.item_id, item.man_name, item.item_type, item.price, item.service_date, item.damage_indicator])

# Create Item type dict LaptopInventory.csv, PhoneInventory.csv
inventory_type_dict = {}

for item in full_inventory_list:
    item_type = item.item_type.replace(' ', '')

    if item_type not in inventory_type_dict:
        inventory_type_dict[item_type] = []
    inventory_type_dict[item_type].append(item)

# Sort each item type inventory list by ID (using selection sort)
for item_type, items in inventory_type_dict.items():
    for i in range(len(items)):
        min_index = i
        for j in range(i + 1, len(items)):
            if items[j].item_id < items[min_index].item_id:
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]

    filename = f"{item_type}Inventory.csv"

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Item ID', 'Manufacturer', 'Price', 'Service Date', 'Damaged'])
        for item in items:
            writer.writerow([item.item_id, item.man_name, item.price, item.service_date, item.damage_indicator])

# Create PastServiceDateInventory.csv
current_date = datetime.date.today()
prev_service_date = []

for item in full_inventory_list:
    if item.service_date != 'none' and item.service_date < current_date:
        prev_service_date.append(item)

# Sort past service date items by service date (using selection sort)
for i in range(len(prev_service_date)):
    min_num = i
    for j in range(i + 1, len(prev_service_date)):
        if prev_service_date[j].service_date < prev_service_date[min_num].service_date:
            min_num = j
    prev_service_date[i], prev_service_date[min_num] = prev_service_date[min_num], prev_service_date[i]

# Output the PastServiceDateInventory.csv
with open('PastServiceDateInventory.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Item ID', 'Manufacturer', 'Item Type', 'Price', 'Service Date', 'Damaged'])
    for item in prev_service_date:
        writer.writerow(
            [item.item_id, item.man_name, item.item_type, item.price, item.service_date, item.damage_indicator])

# Create DamagedInventory.csv
damaged_inventory = []

for item in full_inventory_list:
    if item.damage_indicator:
        damaged_inventory.append(item)

# Sort damaged items by price in order (using selection sort)
for i in range(len(damaged_inventory)):
    max_index = i
    for j in range(i + 1, len(damaged_inventory)):
        if damaged_inventory[j].price > damaged_inventory[max_index].price:
            max_index = j
    damaged_inventory[i], damaged_inventory[max_index] = damaged_inventory[max_index], damaged_inventory[i]

# Output the DamagedInventory.csv
with open('DamagedInventory.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Item ID', 'Manufacturer', 'Item Type', 'Price', 'Service Date', 'Damaged'])
    for item in damaged_inventory:
        writer.writerow(
            [item.item_id, item.man_name, item.item_type, item.price, item.service_date, item.damage_indicator])

# print done to show successful termination
print("Done")
