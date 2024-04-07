from components.rent_car import rent_car
from components.return_vehicle import return_vehicle
from components.main_menu import main_menu

def rents_menu(db_vehicles, db_clients):
    while True:
        try:
            print("\n***RENTS MANAGEMENT***")
            print("Please, select one of the options below")
            option = int(input("1) Rent a Vehicle.\n2) Return a Vehicle.\n3) Return to Previous Menu.\n"))
            
            if option == 1:
                db_vehicles, db_clients = rent_car(db_vehicles,db_clients)
            elif option == 2:
                db_vehicles, db_clients = return_vehicle(db_vehicles,db_clients)
            elif option == 3:
                main_menu(db_vehicles, db_clients)
            else:
                print("The selected option is not valid.")
        except ValueError:
                    print("Please enter one of the valid options.")