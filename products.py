class Product:
    def __init__(self, name, price, quantity):
        if not name or price < 0 or quantity < 0:
            raise Exception("Invalid product values")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            raise Exception("Quantity cannot be negative")

        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()
        else:
            self.activate()

    def is_active(self):
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: ${self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        if quantity <= 0:
            raise Exception("Quantity must be greater than 0")

        if not self.active:
            raise Exception("Product is not active")

        if quantity > self.quantity:
            raise Exception("Not enough items in stock")

        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        return self.price * quantity