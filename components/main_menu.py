from components.fleet_menu import fleet_menu
from components.clients_menu import clients_menu
from components.rents_menu import rents_menu

def main_menu(db_vehicles, db_clients):
    while True:
        try:
            print("\n***MAIN MANAGEMENT***")
            print("Please, select one of the options below")
            option = int(input("1) Fleet Management.\n2) Clients Management.\n3) Rents Management.\n4) Exit\n"))
            
            if option == 1:
                db_vehicles, db_clients = fleet_menu(db_vehicles, db_clients)
            elif option == 2:
                db_vehicles, db_clients = clients_menu(db_vehicles, db_clients)
            elif option == 3:
                db_vehicles, db_clients = rents_menu(db_vehicles, db_clients)
            elif option == 4:
                print("Exiting...")
                break
            else:
                print("The selected option is not valid.")
        except ValueError:
                    print("Please enter one of the valid options.")