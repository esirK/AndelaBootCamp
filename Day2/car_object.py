class Car(object):
    speed=0
    saloon=False
    def __init__(self,name="General",model="GM",car_type=None):
            self.name=name
            self.model=model
            self.car_type=car_type
            if (name=='Porshe' or name=='Koenigsegg'):
                self.num_of_doors=2
            else:
                self.num_of_doors=4
            if (car_type=='trailer'):
                self.num_of_wheels=8
            else:
                self.num_of_wheels=4
            
            if car_type!='trailer':
                self.saloon=True
    def is_saloon(self):
        return self.saloon
