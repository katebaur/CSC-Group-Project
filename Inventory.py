import data

def sum_of_items(item_inventory:dict[data.Color_Item:int]) -> int:
    return sum(item_inventory.values())

def sum_of_all_items(category_1:int, category_2:int, category_3:int) -> int:
    sum = category_1 + category_2 + category_3
    return sum

# Inventory for Tops
# Define what type of tops
Baby_Tee = data.Item(123,'Baby tee',16.99)
Tank_Top = data.Item(124,'Tank Top',14.99)
Tube_Top = data.Item(125,'Tube Top',12.99)
# How many colors in each type of top and how many of each color
BT_Inventory = {data.Color_Item(Baby_Tee,'Pink'):3,data.Color_Item(Baby_Tee,'Yellow'):3,data.Color_Item(Baby_Tee,'Green'):3}
TaT_Inventory = {data.Color_Item(Tank_Top,'Pink'):10,data.Color_Item(Tank_Top,'Yellow'):10,data.Color_Item(Tank_Top,'Green'):10}
TuT_Inventory = {data.Color_Item(Tube_Top,'Pink'):10,data.Color_Item(Tube_Top,'Yellow'):10,data.Color_Item(Tube_Top,'Green'):10}
# The total tops for each type of top
Sum_BT = sum_of_items(BT_Inventory)
Sum_TaT = sum_of_items(TaT_Inventory)
Sum_TuT = sum_of_items(TuT_Inventory)
# A list of the different types of tops
Tops = [Baby_Tee,Tank_Top,Tube_Top]
# An inventory of the different type of tops with the number of the quantity of each top
Tops_Inventory = {Baby_Tee:Sum_BT,Tank_Top:Sum_TaT,Tube_Top:Sum_TuT}
# The total number of tops
Total_Tops = sum_of_all_items(Sum_BT,Sum_TaT,Sum_TaT)


# Inventory for Bottoms
# Define what type of bottoms
Jean_Shorts = data.Item(126,'Jean Shorts',32.99)
Athletic_shorts = data.Item(127,'Athletic Shorts',29.99)
Sweat_shorts = data.Item(128,'Sweat Shorts',14.99)
# How many colors in each type of bottom and how many of each color
JS_Inventory ={data.Color_Item(Jean_Shorts,'Light Blue'):10,data.Color_Item(Jean_Shorts,'Black'):10,data.Color_Item(Jean_Shorts,'Dark Blue'):10}
AS_Inventory = {data.Color_Item(Athletic_shorts,'Light Blue'):19,data.Color_Item(Athletic_shorts,'Black'):7,data.Color_Item(Athletic_shorts,'Dark Blue'):13}
SS_Inventory = {data.Color_Item(Sweat_shorts,'Light Blue'):10,data.Color_Item(Sweat_shorts,'Black'):10,data.Color_Item(Sweat_shorts,'Dark Blue'):10}
# The total bottoms for each type of bottom
Sum_JS = sum_of_items(JS_Inventory)
Sum_AS = sum_of_items(AS_Inventory)
Sum_SS = sum_of_items(SS_Inventory)
# A list of the different types of bottoms
Shorts = [Jean_Shorts,Athletic_shorts,Sweat_shorts]
# An inventory of the different type of bottoms with the number of the quantity of each bottom
Shorts_Inventory = {Jean_Shorts:Sum_JS,Athletic_shorts:Sum_AS,Sweat_shorts: Sum_SS}
# The total number of tops
Total_Bottoms = sum_of_all_items(Sum_JS,Sum_AS,Sum_SS)


# Inventory for Dresses
# Define what type of dresses
Mini_dress = data.Item(130,'Mini Dress',34.99)
Midi_dress = data.Item(131,'Midi Dress',39.99)
Maxi_dress = data.Item(130,'Maxi Dress',40.99)
# How many colors in each type of dress and how many of each color
Mini_Inventory ={data.Color_Item(Mini_dress,'Light Blue'):10,data.Color_Item(Mini_dress,'Black'):10,data.Color_Item(Mini_dress,'Dark Blue'):10}
Midi_Inventory = {data.Color_Item(Midi_dress,'Light Blue'):19,data.Color_Item(Midi_dress,'Black'):7,data.Color_Item(Midi_dress,'Dark Blue'):13}
Maxi_Inventory = {data.Color_Item(Maxi_dress,'Light Blue'):21,data.Color_Item(Maxi_dress,'Black'):10,data.Color_Item(Maxi_dress,'Dark Blue'):19}
# The total dresses for each type of dress
Sum_mini = sum_of_items(Mini_Inventory)
Sum_midi = sum_of_items(Midi_Inventory)
Sum_maxi = sum_of_items(Maxi_Inventory)
# A list of the different types of dresses
Dress = [Mini_dress, Midi_dress, Maxi_dress]
# An inventory of the different type of dress with the number of the quantity of each dress
Dress_Inventory = {Mini_dress:Sum_mini,Midi_dress:Sum_midi,Maxi_dress: Sum_maxi}
# The total number of tops
Total_Dresses = sum_of_all_items(Sum_mini,Sum_midi,Sum_maxi)





