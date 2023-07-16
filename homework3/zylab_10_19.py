# John Rebeles
# PSID: 2039426
class ItemToPurchase:
    def __init__(self, item_name="none", item_price=0, item_quantity=0, item_description="none"):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    # Bottled Water 10 @ $1 = $10
    def print_item(self):
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_price * self.item_quantity}')

    def print_item_description(self):
        print(f'{self.item_name}: {self.item_description}')


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2016"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

    def remove_item(self, item_name):
        for i in self.cart_items:
            if i.item_name != item_name:
                print("Item not found in cart. Nothing removed.")
                break
            else:
                self.cart_items.remove(item_name)

    def modify_(self, item, new_quan):
        for index in self.cart_items:
            if index.item_name != item:
                print("Item not found in cart. Nothing modified.")
                break
            else:
                index.item_quantity = new_quan
        return

    def get_num_items_in_cart(self):
        counter = 0
        for index in self.cart_items:
            counter += index.item_quantity
        return counter

    def get_cost_of_cart(self):
        cost = 0
        for index in self.cart_items:
            cost += (index.item_quantity * index.item_price)
        return cost

    def print_total(self):
        print("\nOUTPUT SHOPPING CART")
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        num_items = self.get_num_items_in_cart()
        if num_items == 0:
            total_cost = 0
            print(f"Number of Items: {num_items}")
            print()
            print("SHOPPING CART IS EMPTY")
            print()
            print(f"Total: ${total_cost}")
        else:
            print(f"Number of Items: {num_items}")
            print()
            total_cost = 0
            for item in self.cart_items:
                item_cost = item.item_quantity * item.item_price
                total_cost += item_cost
                print(f"{item.item_name} {item.item_quantity} @ ${item.item_price} = ${item_cost}")
            print()
            print(f"Total: ${total_cost}")
        print()

    def print_descriptions(self):
        if len(self.cart_items) != 0:
            for index in self.cart_items:
                index.print_item_description()
            return
        else:
            print("\nSHOPPING CART IS EMPTY")
            print()
            return


if __name__ == "__main__":

    def print_menu(shopping_cart):
        print()
        print("MENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items\' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        print()

        while True:
            print("Choose an option:")
            user_choice_input = input()
            if user_choice_input == 'a':
                new_item_name = input()
                new_item_desc = input()
                new_item_price = int(input())
                new_item_quan = int(input())
                new_item = ItemToPurchase(new_item_name, new_item_price, new_item_quan, new_item_desc)
                shopping_cart.add_item(new_item)
            elif user_choice_input == 'r':
                item_to_remove = input()
                shopping_cart.remove_item(item_to_remove)
            elif user_choice_input == 'c':
                item_to_change_quan = input()
                new_item_quan = int(input())
                item_quan = ItemToPurchase(item_to_change_quan, item_quantity=new_item_quan)
                shopping_cart.modify_(item_quan)
            elif user_choice_input == 'i':
                shopping_cart.print_descriptions()
            elif user_choice_input == 'o':
                shopping_cart.print_total()
            elif user_choice_input == 'q':
                break


    customer_name = input("Enter customer's name:")
    print()
    customer_date = input("Enter today's date:")
    print()

    print("\nCustomer name:", customer_name)
    print("Today's date:", customer_date)
    shopping_cart1 = ShoppingCart(customer_name, customer_date)
    print_menu(shopping_cart1)
