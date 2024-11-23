class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def apply_discount(self):
        discount = self.get_discount_rate()
        discounted_price = self.price - (self.price * discount)
        print(f"Discounted price for {self.name} ({self.__class__.__name__}): {discounted_price}")
        return discounted_price

    def calculate_tax(self):
        tax_rate = self.get_tax_rate()
        tax = self.price * tax_rate
        print(f"Tax for {self.name} ({self.__class__.__name__}): {tax}")
        return tax

    def get_discount_rate(self):
        """Subclasses must implement this to provide the discount rate."""
        raise NotImplementedError("Subclass must implement get_discount_rate")

    def get_tax_rate(self):
        """Subclasses must implement this to provide the tax rate."""
        raise NotImplementedError("Subclass must implement get_tax_rate")


class Electronics(Item):
    def get_discount_rate(self):
        return 0.10  # 10% discount

    def get_tax_rate(self):
        return 0.15  # 15% tax


class Clothing(Item):
    def get_discount_rate(self):
        return 0.20  # 20% discount

    def get_tax_rate(self):
        return 0.08  # 8% tax


class Grocery(Item):
    def get_discount_rate(self):
        return 0.05  # 5% discount

    def get_tax_rate(self):
        return 0.02  # 2% tax