from retailitem import RetailItem
class CashRegister():
    def __init__(self, RetailItem):
        self.description = RetailItem.description
        self.units = RetailItem.units
        self.price = RetailItem.price
        self.number = RetailItem.number
        self.RetailItem = RetailItem
    shoppingcart = []
    thetotal = 0
    def purchase_item(self, RetailItem):
        thetotal += self.price * self.units
        item = choice - 1
        shoppingcart.append(item in items)
        return shoppingcart
    def get_total(self, RetailItem):
        return thetotal
    def show_items(self):
        print(shoppingcart)
    def clear(self, description, units, price, number):
        shoppingcart = []
        thetotal = 0
        return shoppingcart and thetotal