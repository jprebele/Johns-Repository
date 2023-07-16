# John Rebeles
# PSID: 2039426
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    # Bottled Water 10 @ $1 = $10
    def print_item(self):
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_price * self.item_quantity}')


if __name__ == "__main__":
    user_name = input("Item 1\nEnter the item name:\n")
    user_price = int(input("Enter the item price:\n"))
    user_quan = int(input("Enter the item quantity:\n"))
    print()
    item1 = ItemToPurchase(user_name, user_price, user_quan)

    user_name2 = input("Item 2\nEnter the item name:\n")
    user_price2 = int(input("Enter the item price:\n"))
    user_quan2 = int(input("Enter the item quantity:\n"))
    item2 = ItemToPurchase(user_name2, user_price2, user_quan2)
    print()

    print("TOTAL COST")
    item1.print_item()
    item2.print_item()
    print()
    print(f'Total: ${(item1.item_quantity * item1.item_price) + (item2.item_quantity * item2.item_price)}')
