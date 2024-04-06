import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.verify_client_rent import verify_client_rent
from components.verify_car_rent import verify_car_rent

def rent_car_UPDATED(db_vehicles, db_clients):
    selected_vehicle = None
    selected_client = None
    
    selected_vehicle, vehicle_index = verify_car_rent(db_vehicles)
    selected_client, client_index = verify_client_rent(db_clients)

def main():
    pass

main()