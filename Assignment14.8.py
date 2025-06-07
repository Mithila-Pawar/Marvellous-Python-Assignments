class Vehicle:
    def start(self):
        print("Vehicle is starting...")

class Car(Vehicle):
    def start(self):
        print("Car engine is starting with a roar!")
        super().start()

v = Vehicle()
v.start()  

c = Car()
c.start()
