# John Rebeles
# PSID: 209426

user_roster = {}


def show_menu():
    print("MENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    print("\nChoose an option:")


def add_player():
    num_to_add = int(input("Enter a new player's jersey number:\n"))
    rating_to_add = int(input("Enter the player's rating:\n"))
    user_roster[num_to_add] = rating_to_add


def del_player():
    num_to_del = int(input("Enter a jersey number:\n"))

    if num_to_del in user_roster:
        del user_roster[num_to_del]


def update_player_rate():
    num_to_update = int(input())

    if num_to_update in user_roster:
        new_num = int(input())
        user_roster.update({num_to_update: new_num})


def players_above_a_rating():
    above_rating = int(input("Enter a rating:\n"))

    print(f'\nABOVE {above_rating}')

    for num, rating in sorted(user_roster.items()):
        if rating > above_rating:
            print(f'Jersey number: {num}, Rating: {rating}')
    print()


def output_roster():
    print('ROSTER')
    for k, val in sorted(user_roster.items()):
        print(f'Jersey number: {k}, Rating: {val}')
    print()


for i in range(5):
    player_num = int(input(f"Enter player {i + 1}'s jersey number:\n"))
    player_rate = int(input(f"Enter player {i + 1}'s rating:\n"))
    print()
    user_roster[player_num] = player_rate

output_roster()

while True:

    show_menu()

    menu_input = input()

    if menu_input == 'a':
        add_player()
    elif menu_input == 'd':
        del_player()
    elif menu_input == 'u':
        update_player_rate()
    elif menu_input == 'r':
        players_above_a_rating()
    elif menu_input == 'o':
        output_roster()
    elif menu_input == 'q':
        break
