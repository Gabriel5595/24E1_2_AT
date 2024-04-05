import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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

def main():
    db_vehicles = []
    db_vehicles = register_car(db_vehicles)
    print(db_vehicles)

main()