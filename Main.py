import Inventory
import data
from Inventory import (BT_Inventory)

# This function takes the items in the given lists, and displays the style and price
def show_items(item_lst:list[data.Item]) -> None: # Author: Sofia Castellanos
    for item in item_lst:
        print('Style: {} Price: {}'.format(item.item_name,item.price))
# This function takes the items in the dictionary and display the available colors
def show_items_color(item_inv_lst:dict) -> None: # Author: Sofia Castellanos
    for key in item_inv_lst.keys():
        print('Color: {}'.format(key.color))

# This function removes items from the shopping cart by asking for the specific item and color
def remove_from_cart(item_name:str, color_choice:str) -> None: #Kate Baur
    item_name = item_name.lower()
    color_choice = color_choice.title()
    item_mapping = {"baby tee": Inventory.Baby_Tee,"tank top": Inventory.Tank_Top,'tube top': Inventory.Tube_Top,'sweat shorts': Inventory.Sweat_shorts,
        'midi dress': Inventory.Midi_dress,'maxi dress': Inventory.Maxi_dress,"jean shorts": Inventory.Jean_Shorts,"athletic shorts": Inventory.Athletic_shorts,
        "mini dress": Inventory.Mini_dress}
    if item_name in item_mapping:
        item = item_mapping[item_name]
        color_item = data.Color_Item(item, color_choice)
        if color_item in shopping_cart:
            if shopping_cart[color_item] > 1:
                shopping_cart[color_item] -= 1
            else:
                del shopping_cart[color_item]
            shopping_cart['Total'] -= item.price
            print(f"Removed {color_choice} {item.item_name} from the shopping cart.")
        else:
            print("Item not found in cart.")
    else:
        print("Invalid item name. Please try again.")

# This function generates a receipt from the items in the cart. It prints the items with the prices and the total
def generate_receipt(cart:dict): #Kate Baur
    print("\n" + "=" * 30)
    print(" " * 10 + "RECEIPT")
    print("=" * 30)

    total = cart.get('Total', 0)
    for item, quantity in cart.items():
        if item != 'Total':
            print(f"{item}: {quantity}")

    print("=" * 30)
    print(f"Total Amount: ${total:.2f}")
    print("=" * 30)
    print("Thank you for shopping with us!\n")





shopping_cart = {'Total': 0}


while True:
    print("Sofia and Kate's Apparel \n Shop for: \n Tops \n Bottoms \n Dresses")
    print('Shopping Cart:', shopping_cart)
    print('Type BACK to go back')
    print('Type Checkout to checkout\nType HOME at any moment to go to home page')
    print('To check Shopping Cart type in SC')
    search = input('What would you like to shop for?')

    if search.lower() == 'sc':
        print('Shopping Cart:',shopping_cart)
        while True:
            # Ask the user if they want to remove an item
            action = input("Would you like to remove an item? (YES/NO): ")

            if action.lower() == 'yes':
                # Ask which item and color the user wants to remove
                item_name = input("Which item would you like to remove? ")
                color_choice = input("What color is the item? ")
                remove_from_cart(item_name,color_choice)
            else:
                break

    elif search.lower() == 'checkout':
        answer = input('Cash or Card: ')
        if answer.lower() == 'cash':
            amount = input('Type in amount: ')
            change = (float(amount) - shopping_cart['Total'])
            print('Change is', change)
            choice = input("Would you like your receipt")
            if choice.lower() == "yes":
                generate_receipt(shopping_cart)
                break

        elif answer.lower() == 'card':
            while True:
                card_number = input('Type in card number: ')
                if len(card_number) < 16 or len(card_number) > 16:
                    print('Invalid Card')
                elif len(card_number) == 16:
                    masked_card = ['x-x-x-x', 'x-x-x-x', 'x-x-x-x', card_number[12:16]]
                    final_card = ' '.join(masked_card)
                    print("Paid with Card:", final_card)
                    choice = input("Would you like your receipt")
                    if choice.lower() == "yes":
                        generate_receipt(shopping_cart)
                        break

    # search browser for tops
    elif search.lower() == 'tops' or search.lower() == 'top':
        exit_shopping = False
        while not exit_shopping:
            print('Available Tops')
            show_items(Inventory.Tops)
            choice = input('Type in what style')
            if choice.lower() == 'back':
                break
            elif choice.lower() == 'sc':
                print('Shopping Cart:',shopping_cart)
            elif choice.lower() == 'home':
                exit_shopping = True
            elif choice.lower() == 'baby tee':
                while not exit_shopping:
                    print('Available Colors')
                    show_items_color(Inventory.BT_Inventory)
                    color_choice = input('Type in what color')
                    if color_choice.lower() == 'sc':
                        print('Shopping Cart:',shopping_cart)
                    elif color_choice.lower() == 'back':
                        break
                    elif color_choice.lower() == 'home':
                        exit_shopping = True
                    elif color_choice.lower() == 'pink':
                        while True:
                            print('Add To Cart?(YES or NO)',Inventory.Baby_Tee,'Color: Pink')
                            answer = input()
                            if answer.lower() == 'yes':
                                if Inventory.BT_Inventory[data.Color_Item(Inventory.Baby_Tee,'Pink')] >= 1:
                                    try:
                                        shopping_cart[data.Color_Item(Inventory.Baby_Tee,'Pink')] += 1
                                    except:
                                        shopping_cart[data.Color_Item(Inventory.Baby_Tee,'Pink')] = 1
                                    Inventory.BT_Inventory[data.Color_Item(Inventory.Baby_Tee, 'Pink')] -= 1
                                    shopping_cart['Total'] += Inventory.Baby_Tee.price
                                    break
                                else:
                                    print('OUT OF STOCK')
                                    break
                            elif answer.lower() == 'no':
                                break
                    elif color_choice.lower() == 'yellow':
                        while True:
                            print('Add To Cart?(YES or NO)',Inventory.Baby_Tee,'Color: Yellow')
                            answer = input()
                            if answer.lower() == 'yes':
                                if Inventory.BT_Inventory[data.Color_Item(Inventory.Baby_Tee,'Yellow')] >= 1:
                                    try:
                                        shopping_cart[data.Color_Item(Inventory.Baby_Tee,'Yellow')] += 1
                                    except:
                                        shopping_cart[data.Color_Item(Inventory.Baby_Tee,'Yellow')] = 1
                                    Inventory.BT_Inventory[data.Color_Item(Inventory.Baby_Tee, 'Yellow')] -= 1
                                    shopping_cart['Total'] += Inventory.Baby_Tee.price
                                    break
                                else:
                                    print('OUT OF STOCK')
                                    break
                            elif answer.lower() == 'no':
                                break
                    elif color_choice.lower() == 'green':
                        while True:
                            print('Add To Cart?(YES or NO)',Inventory.Baby_Tee,'Color: Green')
                            answer = input()
                            if answer.lower() == 'yes':
                                if Inventory.BT_Inventory[data.Color_Item(Inventory.Baby_Tee,'Green')] >= 1:
                                    try:
                                        shopping_cart[data.Color_Item(Inventory.Baby_Tee,'Green')] += 1
                                    except:
                                        shopping_cart[data.Color_Item(Inventory.Baby_Tee,'Green')] = 1
                                    Inventory.BT_Inventory[data.Color_Item(Inventory.Baby_Tee, 'Green')] -= 1
                                    shopping_cart['Total'] += Inventory.Baby_Tee.price
                                    break
                                else:
                                    print('OUT OF STOCK')
                                    break
                            elif answer.lower() == 'no':
                                break
            elif choice.lower() == 'tank top':
                exit_shopping = False
                while not exit_shopping:
                    print('Available Colors')
                    show_items_color(Inventory.TaT_Inventory)
                    color_choice = input('Type in what color')
                    if color_choice.lower() == 'sc':
                        print('Shopping Cart:',shopping_cart)
                    elif color_choice.lower() == 'back':
                        break
                    elif choice.lower() == 'home':
                        exit_shopping = True
                    elif color_choice.lower() == 'pink':
                        while True:
                            print('Add To Cart?(YES or NO)',Inventory.Tank_Top,'Color: Pink')
                            answer = input()
                            if answer.lower() == 'yes':
                                if Inventory.TaT_Inventory[data.Color_Item(Inventory.Tank_Top,'Pink')] >= 1:
                                    try:
                                        shopping_cart[data.Color_Item(Inventory.Tank_Top,'Pink')] += 1
                                    except:
                                        shopping_cart[data.Color_Item(Inventory.Tank_Top,'Pink')] = 1
                                    Inventory.TaT_Inventory[data.Color_Item(Inventory.Tank_Top, 'Pink')] -= 1
                                    shopping_cart['Total'] += Inventory.Tank_Top.price
                                    break
                                else:
                                    print('OUT OF STOCK')
                                    break
                            elif answer.lower() == 'no':
                                break
                    elif color_choice.lower() == 'yellow':
                        while True:
                            print('Add To Cart?(YES or NO)',Inventory.Tank_Top,'Color: Yellow')
                            answer = input()
                            if answer.lower() == 'yes':
                                if Inventory.TaT_Inventory[data.Color_Item(Inventory.Tank_Top,'Yellow')] >= 1:
                                    try:
                                        shopping_cart[data.Color_Item(Inventory.Tank_Top,'Yellow')] += 1
                                    except:
                                        shopping_cart[data.Color_Item(Inventory.Tank_Top,'Yellow')] = 1
                                    Inventory.TaT_Inventory[data.Color_Item(Inventory.Tank_Top, 'Yellow')] -= 1
                                    shopping_cart['Total'] += Inventory.Tank_Top.price
                                    break
                                else:
                                    print('OUT OF STOCK')
                                    break
                            elif answer.lower() == 'no':
                                break
                    elif color_choice.lower() == 'green':
                        while True:
                            print('Add To Cart?(YES or NO)',Inventory.Tank_Top,'Color: Green')
                            answer = input()
                            if answer.lower() == 'yes':
                                if Inventory.TaT_Inventory[data.Color_Item(Inventory.Tank_Top,'Green')] >= 1:
                                    try:
                                        shopping_cart[data.Color_Item(Inventory.Tank_Top,'Green')] += 1
                                    except:
                                        shopping_cart[data.Color_Item(Inventory.Tank_Top,'Green')] = 1
                                    Inventory.TaT_Inventory[data.Color_Item(Inventory.Tank_Top, 'Green')] -= 1
                                    shopping_cart['Total'] += Inventory.Tank_Top.price
                                    break
                                else:
                                    print('OUT OF STOCK')
                                    break
                            elif answer.lower() == 'no':
                                break
            elif choice.lower() == 'tube top':
                exit_shopping = False
                while not exit_shopping:
                    print('Available Colors')
                    show_items_color(Inventory.TuT_Inventory)
                    color_choice = input('Type in what color')
                    if color_choice.lower() == 'sc':
                        print('Shopping Cart:',shopping_cart)
                    elif color_choice.lower() == 'back':
                        break
                    elif choice.lower() == 'home':
                        exit_shopping = True
                    elif color_choice.lower() == 'pink':
                        while True:
                            print('Add To Cart?(YES or NO)',Inventory.Tube_Top,'Color: Pink')
                            answer = input()
                            if answer.lower() == 'yes':
                                if Inventory.TuT_Inventory[data.Color_Item(Inventory.Tube_Top,'Pink')] >= 1:
                                    try:
                                        shopping_cart[data.Color_Item(Inventory.Tube_Top,'Pink')] += 1
                                    except:
                                        shopping_cart[data.Color_Item(Inventory.Tube_Top,'Pink')] = 1
                                    Inventory.TuT_Inventory[data.Color_Item(Inventory.Tube_Top, 'Pink')] -= 1
                                    shopping_cart['Total'] += Inventory.Tube_Top.price
                                    break
                                else:
                                    print('OUT OF STOCK')
                                    break
                            elif answer.lower() == 'no':
                                break
                    elif color_choice.lower() == 'yellow':
                        while True:
                            print('Add To Cart?(YES or NO)',Inventory.Tube_Top,'Color: Yellow')
                            answer = input()
                            if answer.lower() == 'yes':
                                if Inventory.TuT_Inventory[data.Color_Item(Inventory.Tube_Top,'Yellow')] >= 1:
                                    try:
                                        shopping_cart[data.Color_Item(Inventory.Tube_Top,'Yellow')] += 1
                                    except:
                                        shopping_cart[data.Color_Item(Inventory.Tube_Top,'Yellow')] = 1
                                    Inventory.TuT_Inventory[data.Color_Item(Inventory.Tube_Top, 'Yellow')] -= 1
                                    shopping_cart['Total'] += Inventory.Tube_Top.price
                                    break
                            elif answer.lower() == 'no':
                                break
                    elif color_choice.lower() == 'green':
                        while True:
                            print('Add To Cart?(YES or NO)',Inventory.Tube_Top,'Color: Green')
                            answer = input()
                            if answer.lower() == 'yes':
                                if Inventory.TuT_Inventory[data.Color_Item(Inventory.Tube_Top,'Green')] >= 1:
                                    try:
                                        shopping_cart[data.Color_Item(Inventory.Tube_Top,'Green')] += 1
                                    except:
                                        shopping_cart[data.Color_Item(Inventory.Tube_Top,'Green')] = 1
                                    Inventory.TuT_Inventory[data.Color_Item(Inventory.Tube_Top, 'Green')] -= 1
                                    shopping_cart['Total'] += Inventory.Tube_Top.price
                                    break
                            elif answer.lower() == 'no':
                                break
    # search browser for bottoms
    elif search.lower() == 'bottoms' or search.lower() == 'bottom':
        exit_shopping = False
        while not exit_shopping:
            print('Available Bottoms')
            show_items(Inventory.Shorts)
            choice = input('Type in what style')
            if choice.lower() == 'back':
                break
            elif choice.lower() == 'sc':
                print('Shopping Cart:',shopping_cart)
            elif choice.lower() == 'home':
                exit_shopping = True
            elif choice.lower() == 'jean shorts':
                exit_shopping = False
                while not exit_shopping:
                    print('Available Colors')
                    show_items_color(Inventory.JS_Inventory)
                    color_choice = input('Type in what color')
                    if color_choice.lower() == 'sc':
                        print('Shopping Cart:',shopping_cart)
                    elif color_choice.lower() == 'back':
                        break
                    elif choice.lower() == 'home':
                        exit_shopping = True
                    elif color_choice.lower() == 'light blue':
                        while True:
                            print('Add To Cart?(YES or NO)',Inventory.Jean_Shorts,'Color: Light Blue')
                            answer = input()
                            if answer.lower() == 'yes':
                                if Inventory.JS_Inventory[data.Color_Item(Inventory.Jean_Shorts,'Light Blue')] >= 1:
                                    try:
                                        shopping_cart[data.Color_Item(Inventory.Jean_Shorts,'Light Blue')] += 1
                                    except:
                                        shopping_cart[data.Color_Item(Inventory.Jean_Shorts,'Light Blue')] = 1
                                    Inventory.JS_Inventory[data.Color_Item(Inventory.Jean_Shorts, 'Light Blue')] -= 1
                                    shopping_cart['Total'] += Inventory.Jean_Shorts.price
                                    break
                                else:
                                    print('OUT OF STOCK')
                                    break
                            elif answer.lower() == 'no':
                                break
                    elif color_choice.lower() == 'black':
                        while True:
                            print('Add To Cart?(YES or NO)',Inventory.Jean_Shorts,'Color: Black')
                            answer = input()
                            if answer.lower() == 'yes':
                                if Inventory.JS_Inventory[data.Color_Item(Inventory.Jean_Shorts,'Black')] >= 1:
                                    try:
                                        shopping_cart[data.Color_Item(Inventory.Jean_Shorts,'Black')] += 1
                                    except:
                                        shopping_cart[data.Color_Item(Inventory.Jean_Shorts,'Black')] = 1
                                    Inventory.JS_Inventory[data.Color_Item(Inventory.Jean_Shorts, 'Black')] -= 1
                                    shopping_cart['Total'] += Inventory.Jean_Shorts.price
                                    break
                                else:
                                    print('OUT OF STOCK')
                                    break
                            elif answer.lower() == 'no':
                                break
                    elif color_choice.lower() == 'dark blue':
                        while True:
                            print('Add To Cart?(YES or NO)',Inventory.Jean_Shorts,'Color: Dark Blue')
                            answer = input()
                            if answer.lower() == 'yes':
                                if Inventory.JS_Inventory[data.Color_Item(Inventory.Jean_Shorts,'Dark Blue')] >= 1:
                                    try:
                                        shopping_cart[data.Color_Item(Inventory.Jean_Shorts,'Dark Blue')] += 1
                                    except:
                                        shopping_cart[data.Color_Item(Inventory.Jean_Shorts,'Dark Blue')] = 1
                                    Inventory.JS_Inventory[data.Color_Item(Inventory.Jean_Shorts, 'Dark Blue')] -= 1
                                    shopping_cart['Total'] += Inventory.Jean_Shorts.price
                                    break
                                else:
                                    print('OUT OF STOCK')
                                    break
                            elif answer.lower() == 'no':
                                break
            elif choice.lower() == 'athletic shorts':
                exit_shopping = False
                while not exit_shopping:
                    print('Available Colors')
                    show_items_color(Inventory.AS_Inventory)
                    color_choice = input('Type in what color')
                    if color_choice.lower() == 'sc':
                        print('Shopping Cart:',shopping_cart)
                    elif color_choice.lower() == 'back':
                        break
                    elif choice.lower() == 'home':
                        exit_shopping = True
                    elif color_choice.lower() == 'light blue':
                        while True:
                            print('Add To Cart?(YES or NO)',Inventory.Athletic_shorts,'Color: Light Blue')
                            answer = input()
                            if answer.lower() == 'yes':
                                if Inventory.AS_Inventory[data.Color_Item(Inventory.Athletic_shorts,'Light Blue')] >= 1:
                                    try:
                                        shopping_cart[data.Color_Item(Inventory.Athletic_shorts,'Light Blue')] += 1
                                    except:
                                        shopping_cart[data.Color_Item(Inventory.Athletic_shorts,'Light Blue')] = 1
                                    Inventory.AS_Inventory[data.Color_Item(Inventory.Athletic_shorts, 'Light Blue')] -= 1
                                    shopping_cart['Total'] += Inventory.Athletic_shorts.price
                                    break
                                else:
                                    print('OUT OF STOCK')
                                    break
                            elif answer.lower() == 'no':
                                break
                    elif color_choice.lower() == 'black':
                        while True:
                            print('Add To Cart?(YES or NO)',Inventory.Athletic_shorts,'Color: Black')
                            answer = input()
                            if answer.lower() == 'yes':
                                if Inventory.AS_Inventory[data.Color_Item(Inventory.Athletic_shorts,'Black')] >= 1:
                                    try:
                                        shopping_cart[data.Color_Item(Inventory.Athletic_shorts,'Black')] += 1
                                    except:
                                        shopping_cart[data.Color_Item(Inventory.Athletic_shorts,'Black')] = 1
                                    Inventory.AS_Inventory[data.Color_Item(Inventory.Athletic_shorts, 'Black')] -= 1
                                    shopping_cart['Total'] += Inventory.Athletic_shorts.price
                                    break
                                else:
                                    print('OUT OF STOCK')
                                    break
                            elif answer.lower() == 'no':
                                break
                    elif color_choice.lower() == 'dark blue':
                        while True:
                            print('Add To Cart?(YES or NO)',Inventory.Athletic_shorts,'Color: Dark Blue')
                            answer = input()
                            if answer.lower() == 'yes':
                                if Inventory.AS_Inventory[data.Color_Item(Inventory.Athletic_shorts,'Dark Blue')] >= 1:
                                    try:
                                        shopping_cart[data.Color_Item(Inventory.Athletic_shorts,'Dark Blue')] += 1
                                    except:
                                        shopping_cart[data.Color_Item(Inventory.Athletic_shorts,'Dark Blue')] = 1
                                    Inventory.AS_Inventory[data.Color_Item(Inventory.Athletic_shorts, 'Dark Blue')] -= 1
                                    shopping_cart['Total'] += Inventory.Athletic_shorts.price
                                    break
                                else:
                                    print('OUT OF STOCK')
                                    break
                            elif answer.lower() == 'no':
                                break
            elif choice.lower() == 'sweat shorts':
                exit_shopping = False
                while not exit_shopping:
                    print('Available Colors')
                    show_items_color(Inventory.SS_Inventory)
                    color_choice = input('Type in what color')
                    if color_choice.lower() == 'sc':
                        print('Shopping Cart:',shopping_cart)
                    elif color_choice.lower() == 'back':
                        break
                    elif choice.lower() == 'home':
                        exit_shopping = True
                    elif color_choice.lower() == 'light blue':
                        while True:
                            print('Add To Cart?(YES or NO)',Inventory.Sweat_shorts,'Color: Light Blue')
                            answer = input()
                            if answer.lower() == 'yes':
                                if Inventory.SS_Inventory[data.Color_Item(Inventory.Sweat_shorts,'Light Blue')] >= 1:
                                    try:
                                        shopping_cart[data.Color_Item(Inventory.Sweat_shorts,'Light Blue')] += 1
                                    except:
                                        shopping_cart[data.Color_Item(Inventory.Sweat_shorts,'Light Blue')] = 1
                                    Inventory.SS_Inventory[data.Color_Item(Inventory.Sweat_shorts, 'Light Blue')] -= 1
                                    shopping_cart['Total'] += Inventory.Sweat_shorts.price
                                    break
                                else:
                                    print('OUT OF STOCK')
                                    break
                            elif answer.lower() == 'no':
                                break
                    elif color_choice.lower() == 'black':
                        while True:
                            print('Add To Cart?(YES or NO)',Inventory.Sweat_shorts,'Color: Black')
                            answer = input()
                            if answer.lower() == 'yes':
                                if Inventory.SS_Inventory[data.Color_Item(Inventory.Sweat_shorts,'Black')] >= 1:
                                    try:
                                        shopping_cart[data.Color_Item(Inventory.Sweat_shorts,'Black')] += 1
                                    except:
                                        shopping_cart[data.Color_Item(Inventory.Sweat_shorts,'Black')] = 1
                                    Inventory.SS_Inventory[data.Color_Item(Inventory.Sweat_shorts, 'Black')] -= 1
                                    shopping_cart['Total'] += Inventory.Sweat_shorts.price
                                    break
                                else:
                                    print('OUT OF STOCK')
                                    break
                            elif answer.lower() == 'no':
                                break
                    elif color_choice.lower() == 'dark blue':
                        while True:
                            print('Add To Cart?(YES or NO)',Inventory.Sweat_shorts,'Color: Dark Blue')
                            answer = input()
                            if answer.lower() == 'yes':
                                if Inventory.SS_Inventory[data.Color_Item(Inventory.Sweat_shorts,'Dark Blue')] >= 1:
                                    try:
                                        shopping_cart[data.Color_Item(Inventory.Sweat_shorts,'Dark Blue')] += 1
                                    except:
                                        shopping_cart[data.Color_Item(Inventory.Sweat_shorts,'Dark Blue')] = 1
                                    Inventory.SS_Inventory[data.Color_Item(Inventory.Sweat_shorts, 'Dark Blue')] -= 1
                                    shopping_cart['Total'] += Inventory.Sweat_shorts.price
                                    break
                                else:
                                    print('OUT OF STOCK')
                                    break
                            elif answer.lower() == 'no':
                                break
    elif search.lower() == 'dresses' or search.lower() == 'dress':
        exit_shopping = False
        while not exit_shopping:
            print('Available Dresses')
            show_items(Inventory.Dress)
            choice = input('Type in what style')
            if choice.lower() == 'back':
                break
            elif choice.lower() == 'sc':
                print('Shopping Cart:',shopping_cart)
            elif choice.lower() == 'mini dress':
                exit_shopping = False
                while not exit_shopping:
                    print('Available Colors')
                    show_items_color(Inventory.Mini_Inventory)
                    color_choice = input('Type in what color')
                    if color_choice.lower() == 'sc':
                        print('Shopping Cart:',shopping_cart)
                    elif color_choice.lower() == 'back':
                        break
                    elif choice.lower() == 'home':
                        exit_shopping = True
                    elif color_choice.lower() == 'light blue':
                        while True:
                            print('Add To Cart?(YES or NO)',Inventory.Mini_dress,'Color: Light Blue')
                            answer = input()
                            if answer.lower() == 'yes':
                                if Inventory.Mini_Inventory[data.Color_Item(Inventory.Mini_dress,'Light Blue')] >= 1:
                                    try:
                                        shopping_cart[data.Color_Item(Inventory.Mini_dress,'Light Blue')] += 1
                                    except:
                                        shopping_cart[data.Color_Item(Inventory.Mini_dress,'Light Blue')] = 1
                                    Inventory.Mini_Inventory[data.Color_Item(Inventory.Mini_dress, 'Light Blue')] -= 1
                                    shopping_cart['Total'] += Inventory.Mini_dress.price
                                    break
                                else:
                                    print('OUT OF STOCK')
                                    break
                            elif answer.lower() == 'no':
                                break
                    elif color_choice.lower() == 'black':
                        while True:
                            print('Add To Cart?(YES or NO)',Inventory.Mini_dress,'Color: Black')
                            answer = input()
                            if answer.lower() == 'yes':
                                if Inventory.Mini_Inventory[data.Color_Item(Inventory.Mini_dress,'Black')] >= 1:
                                    try:
                                        shopping_cart[data.Color_Item(Inventory.Mini_dress,'Black')] += 1
                                    except:
                                        shopping_cart[data.Color_Item(Inventory.Mini_dress,'Black')] = 1
                                    Inventory.Mini_Inventory[data.Color_Item(Inventory.Mini_dress, 'Black')] -= 1
                                    shopping_cart['Total'] += Inventory.Mini_dress.price
                                    break
                                else:
                                    print('OUT OF STOCK')
                                    break
                            elif answer.lower() == 'no':
                                break
                    elif color_choice.lower() == 'dark blue':
                        while True:
                            print('Add To Cart?(YES or NO)',Inventory.Mini_dress,'Color: Dark Blue')
                            answer = input()
                            if answer.lower() == 'yes':
                                if Inventory.Mini_Inventory[data.Color_Item(Inventory.Mini_dress,'Dark Blue')] >= 1:
                                    try:
                                        shopping_cart[data.Color_Item(Inventory.Mini_dress,'Dark Blue')] += 1
                                    except:
                                        shopping_cart[data.Color_Item(Inventory.Mini_dress,'Dark Blue')] = 1
                                    Inventory.Mini_Inventory[data.Color_Item(Inventory.Mini_dress, 'Dark Blue')] -= 1
                                    shopping_cart['Total'] += Inventory.Mini_dress.price
                                    break
                                else:
                                    print('OUT OF STOCK')
                                    break
                            elif answer.lower() == 'no':
                                break
            elif choice.lower() == 'midi dress':
                exit_shopping = False
                while not exit_shopping:
                    print('Available Colors')
                    show_items_color(Inventory.Midi_Inventory)
                    color_choice = input('Type in what color')
                    if color_choice.lower() == 'sc':
                        print('Shopping Cart:',shopping_cart)
                    elif color_choice.lower() == 'back':
                        break
                    elif choice.lower() == 'home':
                        exit_shopping = True
                    elif color_choice.lower() == 'light blue':
                        while True:
                            print('Add To Cart?(YES or NO)',Inventory.Midi_dress,'Color: Light Blue')
                            answer = input()
                            if answer.lower() == 'yes':
                                if Inventory.Midi_Inventory[data.Color_Item(Inventory.Midi_dress,'Light Blue')] >= 1:
                                    try:
                                        shopping_cart[data.Color_Item(Inventory.Midi_dress,'Light Blue')] += 1
                                    except:
                                        shopping_cart[data.Color_Item(Inventory.Midi_dress,'Light Blue')] = 1
                                    Inventory.Midi_Inventory[data.Color_Item(Inventory.Midi_dress, 'Light Blue')] -= 1
                                    shopping_cart['Total'] += Inventory.Midi_dress.price
                                    break
                                else:
                                    print('OUT OF STOCK')
                                    break
                            elif answer.lower() == 'no':
                                break
                    elif color_choice.lower() == 'black':
                        while True:
                            print('Add To Cart?(YES or NO)', Inventory.Midi_dress, 'Color: Black')
                            answer = input()
                            if answer.lower() == 'yes':
                                if Inventory.Midi_Inventory[data.Color_Item(Inventory.Midi_dress, 'Black')] >= 1:
                                    try:
                                        shopping_cart[data.Color_Item(Inventory.Midi_dress, 'Black')] += 1
                                    except:
                                        shopping_cart[data.Color_Item(Inventory.Midi_dress, 'Black')] = 1
                                    Inventory.Midi_Inventory[data.Color_Item(Inventory.Midi_dress, 'Black')] -= 1
                                    shopping_cart['Total'] += Inventory.Midi_dress.price
                                    break
                                else:
                                    print('OUT OF STOCK')
                                    break
                            elif answer.lower() == 'no':
                                break
                    elif color_choice.lower() == 'dark blue':
                        while True:
                            print('Add To Cart?(YES or NO)',Inventory.Midi_dress,'Color: Dark Blue')
                            answer = input()
                            if answer.lower() == 'yes':
                                if Inventory.Midi_Inventory[data.Color_Item(Inventory.Midi_dress,'Dark Blue')] >= 1:
                                    try:
                                        shopping_cart[data.Color_Item(Inventory.Midi_dress,'Dark Blue')] += 1
                                    except:
                                        shopping_cart[data.Color_Item(Inventory.Midi_dress,'Dark Blue')] = 1
                                    Inventory.Midi_Inventory[data.Color_Item(Inventory.Midi_dress, 'Dark Blue')] -= 1
                                    shopping_cart['Total'] += Inventory.Midi_dress.price
                                    break
                                else:
                                    print('OUT OF STOCK')
                                    break
                            elif answer.lower() == 'no':
                                break
            elif choice.lower() == 'maxi dress':
                exit_shopping = False
                while not exit_shopping:
                    print('Available Colors')
                    show_items_color(Inventory.Maxi_Inventory)
                    color_choice = input('Type in what color')
                    if color_choice.lower() == 'sc':
                        print('Shopping Cart:',shopping_cart)
                    elif color_choice.lower() == 'back':
                        break
                    elif choice.lower() == 'home':
                        exit_shopping = True
                    elif color_choice.lower() == 'light blue':
                        while True:
                            print('Add To Cart?(YES or NO)',Inventory.Maxi_dress,'Color: Light Blue')
                            answer = input()
                            if answer.lower() == 'yes':
                                if Inventory.Maxi_Inventory[data.Color_Item(Inventory.Maxi_dress,'Light Blue')] >= 1:
                                    try:
                                        shopping_cart[data.Color_Item(Inventory.Maxi_dress,'Light Blue')] += 1
                                    except:
                                        shopping_cart[data.Color_Item(Inventory.Maxi_dress,'Light Blue')] = 1
                                    Inventory.Maxi_Inventory[data.Color_Item(Inventory.Maxi_dress, 'Light Blue')] -= 1
                                    shopping_cart['Total'] += Inventory.Maxi_dress.price
                                    break
                                else:
                                    print('OUT OF STOCK')
                                    break
                            elif answer.lower() == 'no':
                                break
                    elif color_choice.lower() == 'black':
                        while True:
                            print('Add To Cart?(YES or NO)',Inventory.Maxi_dress,'Color: Black')
                            answer = input()
                            if answer.lower() == 'yes':
                                if Inventory.Maxi_Inventory[data.Color_Item(Inventory.Maxi_dress,'Black')] >= 1:
                                    try:
                                        shopping_cart[data.Color_Item(Inventory.Maxi_dress,'Black')] += 1
                                    except:
                                        shopping_cart[data.Color_Item(Inventory.Maxi_dress,'Black')] = 1
                                    Inventory.Maxi_Inventory[data.Color_Item(Inventory.Maxi_dress, 'Black')] -= 1
                                    shopping_cart['Total'] += Inventory.Maxi_dress.price
                                    break
                                else:
                                    print('OUT OF STOCK')
                                    break
                            elif answer.lower() == 'no':
                                break
                    elif color_choice.lower() == 'dark blue':
                        while True:
                            print('Add To Cart?(YES or NO)',Inventory.Maxi_dress,'Color: Dark Blue')
                            answer = input()
                            if answer.lower() == 'yes':
                                if Inventory.Maxi_Inventory[data.Color_Item(Inventory.Maxi_dress,'Dark Blue')] >= 1:
                                    try:
                                        shopping_cart[data.Color_Item(Inventory.Maxi_dress,'Dark Blue')] += 1
                                    except:
                                        shopping_cart[data.Color_Item(Inventory.Maxi_dress,'Dark Blue')] = 1
                                    Inventory.Maxi_Inventory[data.Color_Item(Inventory.Maxi_dress, 'Dark Blue')] -= 1
                                    shopping_cart['Total'] += Inventory.Maxi_dress.price
                                    break
                                else:
                                    print('OUT OF STOCK')
                                    break
                            elif answer.lower() == 'no':
                                break
