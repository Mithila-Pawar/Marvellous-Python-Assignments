class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Product):
            return self.price == other.price
        return False

p1 = Product("Laptop", 1500)
p2 = Product("Tablet", 1500)
p3 = Product("Phone", 800)

print(p1 == p2)  
print(p1 == p3)  