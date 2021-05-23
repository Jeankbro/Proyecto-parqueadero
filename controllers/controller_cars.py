from controllers import controller_parking_lot


def create_car(brand, type, id):
    from model import car
    car_brand = brand
    car_type = type
    car_id = id

    car = car.Car(car_brand, car_type, car_id, "hola", "hola2")
    append_car(car)


def append_car(car):
    controller_parking_lot.append_car(car)



