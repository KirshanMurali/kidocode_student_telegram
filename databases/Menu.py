
import json

class Menu:
    def __init__(self, filename):
        self.filename = filename
    
    def get_menu(self, spec_item=None):
        with open(self.filename) as f:
            menu = []
            data = json.load(f)
            for key, value in data.items():
                # if spec_item == "name":
                #     menu.append(value["name"])
                # elif spec_item == "photo":
                #     menu.append(value["photo"])
                # elif spec_item == "price":
                #     menu.append(value["price"])
                # else:
                #     menu.append(value)
                if spec_item in value.keys():
                    menu.append(value[spec_item])
                else:
                    menu.append(value)
        return menu
    
    def add_item(self, foodname, price, image):
        with open(self.filename) as f:
            menu = json.load(f)
        
        menu_file = open(self.filename, "ab")
        food_item = "food_{}".format(len(menu)+1)
        menu[food_item] = {"name": foodname, "price": price, "photo": image}
        menu_file.close()
        return menu