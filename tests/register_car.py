import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.request_plate import request_plate

def register_car(db_vehicles):
    plate = request_plate()
    TODO: CREATE FUNCTION request_model()
    TODO: CREATE FUNCTION request_category()
    TODO: ADD IT ALL TO A NEW LIST
    TODO: ADD NEW LIST TO db_vehicles

def main():
    db_vehicles = []
    register_car(db_vehicles)

main()