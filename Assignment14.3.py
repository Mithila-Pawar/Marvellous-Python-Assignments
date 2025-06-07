class Book:
    def __init__(self, price):
        self.__price = price

    def get_price(self):
        return self.__price
    
    def set_price(self, new_price):
        if new_price >= 0:
            self.__price = new_price
        else:
            print("Price cannot be negative.")

book1 = Book(300)

print("Initial Price:", book1.get_price())  
book1.set_price(450)                      
print("Updated Price:", book1.get_price())

book1.set_price(-100) 
