# John Rebles
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


# function to get data from csv
def csv_reader(csv_file, index):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        extracted_data = {row[index]: row for row in reader}
    return extracted_data


# putting data from csv files into variables
manufacturer_data = csv_reader('ManufacturerList.csv', 0)
price_data = csv_reader('PriceList.csv', 0)
service_data = csv_reader('ServiceDatesList.csv', 0)

# create inventory objects and store them in the full_inventory list
full_inventory_list = []

for item_id, data in manufacturer_data.items():
    manufacturer_name, inventory_type, damage_indicator = data[:3]
    price = int(price_data.get(item_id, [0, 0])[1])
    serv_date = service_data.get(item_id, [0, 'none'])[1]
    service_date = datetime.datetime.strptime(serv_date, '%m/%d/%Y').date()\
        if serv_date != 'none' else 'none'
    inventory_item = InventoryItems(item_id, manufacturer_name, inventory_type, damage_indicator, price, service_date)
    full_inventory_list.append(inventory_item)

# Sort the full inventory list by manufacturer
full_inventory_list.sort(key=lambda item: item.man_name)

# Output the FullInventory.csv
with open('FullInventory.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Item ID', 'Manufacturer', 'Item Type', 'Price', 'Service Date', 'Damaged'])

    for item in full_inventory_list:
        writer.writerow([item.item_id, item.man_name, item.item_type, item.price, item.service_date, item.damage_indicator])

# Create Item type dict LaptopInventory.csv, PhoneInventory.csv...
inventory_type_dict = {}

for item in full_inventory_list:
    item_type = item.item_type.replace(' ', '') 

    if item_type not in inventory_type_dict:
        inventory_type_dict[item_type] = []
    inventory_type_dict[item_type].append(item)

# Sort each item type inventory list by ID
for item_type, items in inventory_type_dict.items():
    items.sort(key=lambda item: item.item_id)
    filename = f"{item_type}Inventory.csv"

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Item ID', 'Manufacturer', 'Price', 'Service Date', 'Damaged'])
        for item in items:
            writer.writerow([item.item_id, item.man_name, item.price, item.service_date, item.damage_indicator])

# Create PastServiceDateInventory.csv
current_date = datetime.date.today()
prev_service_date = list(filter(lambda item: item.service_date != 'none' and item.service_date < current_date, full_inventory_list))

# Sort past service date items by service date
prev_service_date.sort(key=lambda item: item.service_date)

# Output the PastServiceDateInventory.csv
with open('PastServiceDateInventory.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Item ID', 'Manufacturer', 'Item Type', 'Price', 'Service Date', 'Damaged'])
    for item in prev_service_date:
        writer.writerow([item.item_id, item.man_name, item.item_type, item.price, item.service_date, item.damage_indicator])

# Create DamagedInventory.csv
damaged_inventory = [item for item in full_inventory_list if item.damage_indicator]

# Sort damaged items by price
damaged_inventory.sort(key=lambda item: item.price, reverse=True)

# Output the DamagedInventory.csv
with open('DamagedInventory.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Item ID', 'Manufacturer', 'Item Type', 'Price', 'Service Date', 'Damaged'])
    for item in damaged_inventory:
        writer.writerow([item.item_id, item.man_name, item.item_type, item.price, item.service_date, item.damage_indicator])

print("Done")
