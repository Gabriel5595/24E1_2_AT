from components.register_user import register_user
from components.request_client_search import request_client_search

def clients_menu(db_vehicles, db_clients):
    while True:
        try:
            print("\n***CLIENTS MANAGEMENT***")
            print("Please, select one of the options below")
            option = int(input("1) Register Client.\n2) Search Client.\n3) Return to Previous Menu.\n"))
            
            if option == 1:
                db_clients = register_user(db_clients)
            elif option == 2:
                request_client_search(db_clients)
            elif option == 3:
                return db_vehicles, db_clients
            else:
                print("The selected option is not valid.")
        except ValueError:
                    print("Please enter one of the valid options.")