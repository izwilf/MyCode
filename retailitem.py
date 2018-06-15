class RetailItem:
    def __init__(self, description, units, price, number):
        self.description = description
        self.units = units
        self.price = price
        self.number = number
    def set_item_description(self, description):
        self.description = description
    def set_units(self, units):
        self.units = units
    def set_price(self, price):
        self.price = price
    def set_number(self, number):
        self.number = number
    def get_item_description(self):
        return self.description
    def get_units(self):
        return self.units
    def get_price(self):
        return self.price
    def get_number(self):
        return self.number