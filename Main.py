import Inventory
import data
from Inventory import BT_Inventory


def show_items(item_lst:list[data.Item]):
    for item in item_lst:
        print('Style: {} Price: {}'.format(item.item_name,item.price))

def show_items_color(item_inv_lst:dict):
    for key in item_inv_lst.keys():
        print('Color: {}'.format(key.color))





shopping_cart = {}
print("Sofia and Kate's Apparel \n Shop for: \n Tops \n Bottoms \n Dresses")
print('Shopping Cart:', shopping_cart)
print("Type EXIT to leave.\nType BACK to go back")

while True:
    search = input('What would you like to shop for? To check Shopping Cart type in SC')

    if search.lower() == 'sc':
        print('Shopping Cart:',shopping_cart)

    elif search.lower() == 'exit':
        break

    elif search.lower() == 'tops' or search.lower() == 'top':
        while True:
            print('Available Tops')
            show_items(Inventory.Tops)
            choice = input('Type in what style')
            if choice.lower() == 'back':
                break
            elif choice.lower() == 'sc':
                print('Shopping Cart:',shopping_cart)
            elif choice.lower() == 'baby tee':
                while True:
                    print('Available Colors')
                    show_items_color(Inventory.BT_Inventory)
                    color_choice = input('Type in what color')
                    if color_choice.lower() == 'sc':
                        print('Shopping Cart:',shopping_cart)
                    elif color_choice.lower() == 'back':
                        break
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
                                    break
                                else:
                                    print('OUT OF STOCK')
                                    break
                            elif answer.lower() == 'no':
                                break
            elif choice.lower() == 'tank top':
                while True:
                    print('Available Colors')
                    show_items_color(Inventory.TaT_Inventory)
                    color_choice = input('Type in what color')
                    if color_choice.lower() == 'sc':
                        print('Shopping Cart:',shopping_cart)
                    elif color_choice.lower() == 'back':
                        break
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
                                    break
                                else:
                                    print('OUT OF STOCK')
                                    break
                            elif answer.lower() == 'no':
                                break
            elif choice.lower() == 'tube top':
                while True:
                    print('Available Colors')
                    show_items_color(Inventory.TuT_Inventory)
                    color_choice = input('Type in what color')
                    if color_choice.lower() == 'sc':
                        print('Shopping Cart:',shopping_cart)
                    elif color_choice.lower() == 'back':
                        break
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
                                    break
                            elif answer.lower() == 'no':
                                break













