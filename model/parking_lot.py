class Parking_lot():
    def __init__(self, parking_lot_name):
        self.__parking_lot_name = parking_lot_name
        self.__cars = []
        self.__money = 0

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

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, money):
        self.__money += money

    def add_car(self, car):
        self.cars = car

    def delete_car(self, car):
        self.cars.remove(car)

