import Inventory
import data



def show_items(item_lst:list[data.Item]) -> None: # Sofia Castellanos
    for item in item_lst:
        print('Style: {} Price: {}'.format(item.item_name,item.price))
# This function takes the items in the dictionary and display the available colors
def show_items_color(item_inv_lst:dict) -> None: #Sofia Castellanos
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
def generate_receipt(cart:dict) -> None: #Kate Baur
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