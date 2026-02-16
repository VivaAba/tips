class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ShopingCart:
    def __init__(self):

        self.items = []
    
    def addItem(self, Item):

        self.items.append(Item)
        
        print(self.items)

    def removeItem(self,Item):

        self.items.remove(Item)

    def showItem(self):

        for i in self.items:
            print(i.name)
    
    def calculateTotal(self):
        a = 0
        for i in self.items:
            a += i.price
        print(a)

item1 = Item('Cola', 3000)
item2 = Item('Milk', 5000)

cart1 = ShopingCart()
cart1.addItem(item1)
cart1.addItem(item2)
cart1.removeItem(item1)
cart1.showItem()
cart1.calculateTotal()