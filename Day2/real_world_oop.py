class Car(object):
    car_ratting=1.04
    number_of_wheels=4
    numberOfCars=0
    def __init__(self,carName,carType,price):
        self.carName=carName
        self.carType=carType
        self.price=price
        self.description=str(carName)+'.'+str(carType)+' Costing '+str(price)
        Car.numberOfCars+=1

    def displayTotalNumberOfCars(self):
        print "Total Cars %d"%Car.numberOfCars
        
    def car_name_and_model(self):
        return self.carName+' '+self.carType
    def raise_rateing(self,raise_amt):
        self.price=int(self.price*self.raise_amt)

class Truck(Car):#Inheritance
    number_of_wheels=6#Information Hideing
    def __init__(self,carName,carType,price,weight):
        super(Truck,self).__init__(carName,carType,price)
        self.weight=weight

class Matatu(Car):
    def __init__(self,carName,carType,price,number_of_passagers,places_of_operation):
        super(Matatu,self).__init__(carName,carType,price)
        self.number_of_passagers=number_of_passagers
        if places_of_operation is None:
            self.places_of_operation=[]
        else:
            self.places_of_operation=places_of_operation

    def add_place_of_operation(self,place_of_operation):
        if place_of_operation not in self.places_of_operation:
            self.places_of_operation.append(place_of_operation)
    def remove_place_of_operation(self,place_of_operation):
        if place_of_operation in self.places_of_operation:
            self.places_of_operation.remove(place_of_operation)
    def routes_of_operation(self):
        routes=[]
        for route in self.places_of_operation:
            routes.append(route)
        return routes
    

car_1=Car('Toyota','Colora',"KSH 350,000")
car_2=Car('Pigeot','max',"KSH 725,000")
truck_1=Truck('Izuzu','Dmax',"KSH 3,500,000",'5 Tones')

matatu_1=Matatu('Nissan','Box',"700,000","7 Seater",["Nyahururu"])
matatu_1.add_place_of_operation("Nairobi")



print car_1.car_name_and_model()+' '
print truck_1.car_name_and_model()+" Weighn "+truck_1.weight

print matatu_1.car_name_and_model()+" Carraying "+matatu_1.number_of_passagers+" Operating Withing "+str(matatu_1.routes_of_operation())

truck_1.displayTotalNumberOfCars()

