import unittest
from idlelib.config import InvalidTheme

import Inventory
import codes
import data
from Main import shopping_cart


class MyTestCase(unittest.TestCase):
    def test_sum_of_items1(self):
        input = Inventory.TuT_Inventory
        expected = 30
        actual = Inventory.sum_of_items(input)
        self.assertEqual(expected,actual)
    def test_sum_of_items2(self):
        input = Inventory.Mini_Inventory
        expected = 44
        actual = Inventory.sum_of_items(input)
        self.assertEqual(expected,actual)

    def test_sum_of_all_items1(self):
        input1 = Inventory.Sum_BT
        input2 = Inventory.Sum_JS
        input3 = Inventory.Sum_TaT
        expected = 69
        actual = Inventory.sum_of_all_items(input3,input2,input1)
        self.assertEqual(expected,actual)
    def test_sum_of_all_items2(self):
        input1 = Inventory.Sum_AS
        input2 = Inventory.Sum_maxi
        input3 = Inventory.Sum_SS
        expected = 119
        actual = Inventory.sum_of_all_items(input3,input2,input1)
        self.assertEqual(expected,actual)

    def test_show_items1(self):
        input = Inventory.Tops
        expected = 'Style: Baby tee Price: 16.99 Style: Tank Top Price: 14.99 Style: Tube Top Price: 12.99'
        codes.show_items(input)
    def test_show_items2(self):
        input = Inventory.Shorts
        expected = 'Style: Jean Shorts Price: 32.99 Style: Athletic Shorts Price: 29.99 Style: Sweat Shorts Price: 14.99'
        codes.show_items(input)

    def test_show_items_color1(self):
        input = Inventory.AS_Inventory
        expected = 'Color: Light Blue Color: Black Color: Dark Blue'
        codes.show_items_color(input)
    def test_show_items_color2(self):
        input = Inventory.BT_Inventory
        expected = 'Color: Pink Color: Yellow Color: Green'
        codes.show_items_color(input)

    def test_generate_receipt1(self):
        sc = {'Total':16.99, data.Color_Item(Inventory.Baby_Tee,'Pink'):1}
        expected = ('==============================RECEIPT=============================='
                    'Item Baby tee, Price 16.99, Color Pink: 1)'
                    '=============================='
                    'Total Amount: $16.99'
                    '=============================='
                    'Thank you for shopping with us!')
        codes.generate_receipt(sc)
    def test_generate_receipt2(self):
        sc = {'Total':123, data.Color_Item(Inventory.Baby_Tee,'Pink'):2,data.Color_Item(Inventory.Baby_Tee,'Green'):1 }
        expected = ('==============================RECEIPT=============================='
                    'Item Baby tee, Price 16.99, Color Pink: 2)'
                    'Item Baby tee, Price 16.99, Color Green: 1'
                    '=============================='
                    'Total Amount: $50.97'
                    '=============================='
                    'Thank you for shopping with us!')
        codes.generate_receipt(sc)

if __name__ == '__main__':
    unittest.main()
