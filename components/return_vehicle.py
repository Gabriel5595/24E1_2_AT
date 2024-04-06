from components.request_cpf import request_cpf
from components.calculate_price import calculate_price

def return_vehicle(db_vehicles, db_clients):
    cpf = request_cpf()
    selected_client = None
    client_index = None
    selected_vehicle = None
    vehicle_index = None
    
    for client in range(len(db_clients)):
        if cpf in db_clients[client][0]:
            selected_client = db_clients[client]
            client_index = client
    
    for vehicle in range(len(db_vehicles)):
        if selected_client[4] in db_vehicles[vehicle][0]:
            selected_vehicle = db_vehicles[vehicle]
            vehicle_index = vehicle
    
    if selected_client == None:
            while True:
                try:
                    print("No client could be found with that CPF. Would you like to try again or exit?")
                    option = int(input("1) Try again.\n2) Exit.\n"))
                    
                    if option == 1:
                        return_vehicle(db_vehicles, db_clients)
                    elif option == 2:
                        break
                    else:
                        print("The selected option is not valid.")
                    break
                except ValueError:
                    print("Please enter one of the valid options.")
    else:

        print(f"The price calculated for this car is ${calculate_price(selected_vehicle[2])}")
        
        db_vehicles[vehicle_index][3] = -1
        db_clients[client_index][4] = None
        
        return db_vehicles, db_clients