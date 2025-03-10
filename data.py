class Item: # Author: Sofia Castellanos
    def __init__(self,item_id,item_name,price):
        self.item_id = item_id  #each item id will be unique
        self.item_name = item_name
        self.price = price
    def __str__(self) -> str:
        return 'Item {}, Price {}'.format(self.item_name,self.price)
    def __repr__(self)-> str:
        return 'Item {}, Price {}'.format(self.item_name,self.price)

class Color_Item: # Author: Kate Baur
    def __init__(self,item:Item, color:str):
        self.item = item
        self.color = color
    def __str__(self):
        return '{}, Color {}'.format(self.item,self.color)
    def __repr__(self):
        return '{}, Color {}'.format(self.item,self.color)
    def __eq__(self, other):
        return isinstance(other, Color_Item) and self.item.item_id == other.item.item_id and self.color == other.color
    def __hash__(self):
        return hash((self.item.item_id, self.color))

