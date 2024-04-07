from components.register_car import register_car
from components.request_vehicle_search_availability import request_vehicle_search_availability
from components.request_vehicle_search_plate import request_vehicle_search_plate
from components.main_menu import main_menu

def fleet_menu(db_vehicles, db_clients):
    while True:
        try:
            print("\n***FLEET MANAGEMENT***")
            print("Please, select one of the options below")
            option = int(input("1) Register Vehicle.\n2) Search by Plate.\n3) Search by Availability.\n4) Return to Previous Menu.\n"))
            
            if option == 1:
                db_vehicles = register_car(db_vehicles)
            elif option == 2:
                request_vehicle_search_plate(db_vehicles)
            elif option == 3:
                request_vehicle_search_availability(db_vehicles)
            elif option == 4:
                main_menu(db_vehicles, db_clients)
            else:
                print("The selected option is not valid.")
        except ValueError:
                    print("Please enter one of the valid options.")