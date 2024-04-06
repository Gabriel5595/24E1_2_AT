from components.request_plate import request_plate
from components.search_vehicle_plate import search_vehicle_plate

def verify_car_rent(db_vehicles):
    plate = request_plate()
    vehicle_index = search_vehicle_plate(db_vehicles, plate)
    
    # Verificar se o carro realmente existe.
    # Caso o carro exista:
    if vehicle_index != []:
        # Verificar se o carro está disponível.
        # Caso o carro exista e esteja disponível:
        if db_vehicles[vehicle_index[0]][3] == -1:
            selected_vehicle = db_vehicles[vehicle_index[0]]
            
            #Confirma se o carro está correto
            while True:
                    try:
                        print(selected_vehicle)
                        print("Is the vehicle correct? If not, would you like to try again or exit?")
                        option = int(input("1) It is correct\n2) Try again.\n3) Exit.\n"))
                        
                        if option == 1:
                            return selected_vehicle, vehicle_index
                        elif option == 2:
                            verify_car_rent(db_vehicles)
                        elif option == 3:
                            selected_vehicle = None
                            vehicle_index = None
                            return selected_vehicle, vehicle_index
                        else:
                            print("The selected option is not valid.")
                        
                    except ValueError:
                        print("Please enter one of the valid options.")
            
        # Caso o carro exista, mas não esteja disponível:
        else:
            while True:
                    try:
                        print("The selected vehicle is unavailable. Would you like to select another or exit?")
                        option = int(input("1) Try again.\n2) Exit.\n"))
                        
                        if option == 1:
                            verify_car_rent(db_vehicles)
                        elif option == 2:
                            selected_vehicle = None
                            vehicle_index = None
                            return selected_vehicle, vehicle_index
                        else:
                            print("The selected option is not valid.")
                        
                    except ValueError:
                        print("Please enter one of the valid options.")
    
    # Caso o carro não exista:
    else:
        while True:
            try:
                print("No vehicle could be found with this plate. Would you like to try again or exit?")
                option = int(input("1) Try again.\n2) Exit.\n"))
                
                if option == 1:
                    verify_car_rent(db_vehicles)
                elif option == 2:
                    selected_vehicle = None
                    vehicle_index = None
                    return selected_vehicle, vehicle_index
                else:
                    print("The selected option is not valid.")
                
            except ValueError:
                print("Please enter one of the valid options.")