class Shop:
    def __init__(self):
        self.items = [
            ["lesser health potion", 12],
            ["greater health potion", 24],
            ["rusty sword", 30],
            ["The Key", 100],
        ]

    def show_item(self):
        shopList = ""
        for i in range(0, len(self.items)):
            item = self.items[i]
            shopList += "* " + str(item[0]) + " costs " + str(item[1]) + " gold.\n"
        return shopList

    def show_list(self):
        return self.items

    def add_item(self, itemName, itemPrice):
        self.items.append([itemName, itemPrice])
