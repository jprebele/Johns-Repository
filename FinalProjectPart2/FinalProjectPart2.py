# John Rebeles
# PSID: 2039426
import csv
import datetime


# inventory class for items in lists
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
        extracted_data = {}
        for row in reader:
            extracted_data[row[index]] = row
    return extracted_data


# a string date and converts to datetime
def convert_to_date(u_date):
    if u_date == 'none':
        return 'none'
    else:
        return datetime.datetime.strptime(u_date, '%m/%d/%Y').date()


# --------------------------------------------PART 2 CODE------------------------------------------------------------
#  function to take a list of items and the price as arguments
#  iterates through list to determine items of similar price

def closest_item(items, price):
    close_item = None
    min_price_diff = float('inf')

    for item in items:
        if not item.damage_indicator and item.service_date != 'none' and item.price <= price:
            price_diff = price - item.price
            if price_diff < min_price_diff:
                close_item = item
                min_price_diff = price_diff

    return close_item


# interactive queue that a user interacts with to go through inventory
# takes manufacturer name and type to search for matching items
# provides information about items and manufacturers to show closest item, most expensive, etc
def query_inventory(full_inventory_list):
    while True:
        user_input = input("Enter the manufacturer and item type (separated by a space) or 'q' to quit: \n")
        if user_input == 'q':
            break

        words = user_input.split()
        if len(words) != 2:
            print("Invalid input. Please enter the manufacturer and item type separated by a space.\n")
            continue

        manufacturer_name, item_type = words

        matching_items = [item for item in full_inventory_list if
                          item.man_name.lower() == manufacturer_name.lower() and item.item_type.lower() ==
                          item_type.lower()]

        if not matching_items:
            print("No such item in inventory.")
            continue

        expensive_item = None
        closest_item_found = None
        for item in matching_items:
            if not item.damage_indicator and item.service_date != 'none':
                if expensive_item is None or item.price > expensive_item.price:
                    expensive_item = item

        if expensive_item:
            print("Your item is:")
            print(f"Item ID: {expensive_item.item_id}, Manufacturer: {expensive_item.man_name}, "
                  f"Item Type: {expensive_item.item_type}, Price: {expensive_item.price}")

            items_from_other_manufacturers = [item for item in full_inventory_list if
                                              item.man_name != manufacturer_name and
                                              item.item_type == item_type]

            if items_from_other_manufacturers:
                closest_item_found = closest_item(items_from_other_manufacturers, expensive_item.price)

            if closest_item_found:
                print("You may also consider:")
                print(f"Item ID: {closest_item_found.item_id}, Manufacturer: {closest_item_found.man_name}, "
                      f"Item Type: {closest_item_found.item_type}, Price: {closest_item_found.price}")
        else:
            print("No valid items found for this manufacturer and item type.")


# -------------------------------------PART 2 CODE--------------------------------------------------------------------


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

# Sort the full inventory list by manufacturer name (selection sort)
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

# Sort each item type inventory list by ID (selection sort)
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

# Sort past service date items by service date (selection sort)
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

# Sort damaged items by price in order (selection sort)
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
        writer.writerow([item.item_id, item.man_name, item.item_type, item.price, item.service_date,
                         item.damage_indicator])

# print done to show successful termination of program
print("Done")

# calling the query function to start interaction with user
query_inventory(full_inventory_list)
