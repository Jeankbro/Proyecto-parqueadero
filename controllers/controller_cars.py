from controllers import controller_parking_lot
import datetime


def create_car(brand, type, id):
    from model import car
    car_brand = brand
    car_type = type
    car_id = id
    car_date = datetime.datetime.now()
    car = car.Car(car_brand, car_type, car_id, car_date)
    append_car(car)


def append_car(car):
    controller_parking_lot.append_car(car)


def delete_car(car):
    controller_parking_lot.delete_car(car)


def payout(car):
    car_leaving = controller_parking_lot.get_car_by_id(car)
    date_of_access = car_leaving.date_of_access
    time_elapsed = datetime.datetime.now()
    total_time = time_elapsed - date_of_access
    if total_time.seconds//3600 == 0:
        total = 1500
    else:
        total = 1500 * total_time.seconds//3600

    return total




