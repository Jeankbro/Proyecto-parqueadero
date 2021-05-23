from model import parking_lot

parking_lot = parking_lot.Parking_lot("")


def create_parking_lot(name):
    parking_lot.parking_lot_name = name


def append_car(doctor_to_be_added):
    parking_lot.add_car(doctor_to_be_added)


def get_car_by_id(car_to_find):
    for car in parking_lot.cars:
        if car.car_id == car_to_find:
            return car

