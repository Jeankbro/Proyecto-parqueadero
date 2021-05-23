class Car():
    def __init__(self, car_brand, car_type, car_id, date_of_access):
        self.__car_brand = car_brand
        self.__car_type = car_type
        self.__car_id = car_id
        self.__date_of_access = date_of_access

    @property
    def car_brand(self):
        return self.__car_brand

    @car_brand.setter
    def car_brand(self, car_brand):
        self.__car_brand = car_brand

    @property
    def car_type(self):
        return self.__car_type

    @car_type.setter
    def car_type(self, car_type):
        self.__car_type = car_type

    @property
    def car_id(self):
        return self.__car_id

    @car_id.setter
    def car_id(self, car_id):
        self.__car_id = car_id

    @property
    def date_of_access(self):
        return self.__date_of_access

    @date_of_access.setter
    def date_of_access(self, date_of_access):
        self.__date_of_access = date_of_access


