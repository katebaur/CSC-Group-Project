import data

def sum_of_items(item_inventory):
    return sum(item_inventory.values())

Baby_Tee = data.Item(123,'Baby tee',16.99)
Tank_Top = data.Item(124,'Tank Top',14.99)
Tube_Top = data.Item(125,'Tube Top',12.99)

BT_Inventory = {data.Color_Item(Baby_Tee,'Pink'):3,data.Color_Item(Baby_Tee,'Yellow'):3,data.Color_Item(Baby_Tee,'Green'):3}
TaT_Inventory = {data.Color_Item(Tank_Top,'Pink'):10,data.Color_Item(Tank_Top,'Yellow'):10,data.Color_Item(Tank_Top,'Green'):10}
TuT_Inventory = {data.Color_Item(Tube_Top,'Pink'):10,data.Color_Item(Tube_Top,'Yellow'):10,data.Color_Item(Tube_Top,'Green'):10}

Sum_BT = sum_of_items(BT_Inventory)
Sum_TaT = sum_of_items(TaT_Inventory)
Sum_TuT = sum_of_items(TuT_Inventory)

Tops = [Baby_Tee,Tank_Top,Tube_Top]
Tops_Inventory = {Baby_Tee:Sum_BT,Tank_Top:Sum_TaT,Tube_Top:Sum_TuT}



Jean_Shorts = data.Item(126,'Jean Shorts',32.99)


JS_Inventory ={data.Color_Item(Jean_Shorts,'Light Blue'):10,data.Color_Item(Jean_Shorts,'Black'):10,data.Color_Item(Jean_Shorts,'Dark Blue'):10,data.Color_Item(Jean_Shorts,'Blue'):10}




Sum_JS = sum_of_items(JS_Inventory)


Total_Inventory = {Baby_Tee:Sum_BT,Tank_Top:Sum_TaT,Tube_Top:Sum_TuT,Jean_Shorts:Sum_JS}
