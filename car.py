class Car:
    
    def __init__(self, make ,model,year):
        self.make = make
        self.model = model
        self.year = year
    
    
    def drive(self):
        print("The car is moving")
        
    def stop(self):
        print("The car has stopped")