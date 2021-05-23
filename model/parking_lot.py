class Parking_lot():
    def __init__(self, parking_lot_name):
        self.__parking_lot_name = parking_lot_name
        self.__cars = []

    @property
    def parking_lot_name(self):
        return self.__parking_lot_name

    @parking_lot_name.setter
    def parking_lot_name(self, name):
        self.__parking_lot_name = name

    @property
    def cars(self):
        return self.__cars

    @cars.setter
    def cars(self, car):
        self.cars.append(car)

    def add_car(self, car):
        self.cars = car

