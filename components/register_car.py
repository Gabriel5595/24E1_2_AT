from components.request_plate import request_plate
from components.request_model import request_model
from components.request_category import request_category

def register_car(db_vehicles):
    plate = request_plate()
    model = request_model()
    category = request_category()
    availability = -1
    new_vehicle = [plate, model, category, availability]
    db_vehicles.append(new_vehicle)
    return db_vehicles