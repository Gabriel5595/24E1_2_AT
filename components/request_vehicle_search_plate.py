from components.request_plate import request_plate
from components.search_vehicle_plate import search_vehicle_plate
from components.print_vehicle_list import print_vehicle_list

def request_vehicle_search_plate(db_vehicles):
    plate = request_plate()
    indexes = search_vehicle_plate(db_vehicles, plate)
    print_vehicle_list(db_vehicles, indexes)