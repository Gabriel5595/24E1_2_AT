from components.search_vehicle_plate import search_vehicle_plate
from components.request_plate import request_plate
from components.request_cpf import request_cpf

def rent_car(db_vehicles, db_clients):
        selected_vehicle = None
        plate = request_plate()
        
        vehicle_index = search_vehicle_plate(db_vehicles, plate)
        
        # Verifica se o o index do veículo encontrado não está vazio (Veículo encontrado)
        if vehicle_index != []:
            if db_vehicles[vehicle_index[0]][3] == -1:
                print(db_vehicles[vehicle_index[0]])
                while True:
                    try:
                        print("Is the vehicle correct? If not, would you like to try again or exit?")
                        option = int(input("1) It is correct\n2) Try again.\n3) Exit.\n"))
                        
                        if option == 1:
                            selected_vehicle = db_vehicles[vehicle_index[0]]
                        elif option == 2:
                            rent_car(db_vehicles, db_clients)
                        elif option == 3:
                            break
                        else:
                            print("The selected option is not valid.")
                        break
                    except ValueError:
                        print("Please enter one of the valid options.")
            else:
                # Dá a opção de tentar novamente ou sair
                while True:
                    try:
                        print("The selected vehicle is unavailable. Would you like to select another or exit?")
                        option = int(input("1) Try again.\n2) Exit.\n"))
                        
                        if option == 1:
                            rent_car(db_vehicles, db_clients)
                        elif option == 2:
                            break
                        else:
                            print("The selected option is not valid.")
                        break
                    except ValueError:
                        print("Please enter one of the valid options.")
        # Verifica se o o index do veículo encontrado está vazio (Veículo não encontrado)
        else:
            # Dá a opção de tentar novamente ou sair
            while True:
                try:
                    print("The entered plate is not valid. Would you like to try again or exit?")
                    option = int(input("1) Try again.\n2) Exit.\n"))
                    
                    if option == 1:
                        rent_car(db_vehicles, db_clients)
                    elif option == 2:
                        break
                    else:
                        print("The selected option is not valid.")
                    break
                except ValueError:
                    print("Please enter one of the valid options.")
        
        
        selected_client = None
        client_index = None
        cpf = request_cpf()
        
        for client in range(len(db_clients)):
            if cpf in db_clients[client][0]:
                selected_client = db_clients[client]
                client_index = [client]
        if selected_client == None:
            while True:
                try:
                    print("No client could be found with that CPF. Would you like to try again or exit?")
                    option = int(input("1) Try again.\n2) Exit.\n"))
                    
                    if option == 1:
                        rent_car(db_vehicles, db_clients)
                    elif option == 2:
                        break
                    else:
                        print("The selected option is not valid.")
                    break
                except ValueError:
                    print("Please enter one of the valid options.")
        else:
            db_vehicles[vehicle_index[0]][3] = selected_client[0]
            db_clients[client_index[0]][4] = selected_vehicle[0]
            
            return db_vehicles, db_clients