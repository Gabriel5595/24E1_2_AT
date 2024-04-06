import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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

def main():
    db_vehicles = [
    ["JKL0124", "Ford Focus", "Basic", '123.456.789-00'],
    ["MNO3455", "Chevrolet Cruze", "Intermediary", -1],
    ["PQR6786", "Audi A4", "Deluxe", -1],
    ["STU9012", "Volkswagen Golf", "Basic", -1],
    ["VWX2347", "Mercedes-Benz C-Class", "Intermediary", -1],
    ["YZA5678", "Lexus RX", "Deluxe", -1],
    ["BCD8903", "Nissan Altima", "Basic", -1],
    ["EFG1231", "Hyundai Sonata", "Intermediary", -1],
    ["HIJ4564", "Tesla Model 3", "Deluxe", -1],
    ["KLM7895", "Subaru Outback", "Basic", -1],
    ["NOP0123", "Kia Optima", "Intermediary", -1],
    ["QRS3450", "Volvo XC90", "Deluxe", -1],
    ["TUV6787", "Mazda CX-5", "Basic", -1],
    ["VWX9015", "Land Rover Range Rover", "Intermediary", -1],
    ["YZA2346", "Jeep Wrangler", "Deluxe", -1],
    ["BCD5677", "Toyota Camry", "Basic", -1],
    ["EFG8908", "Honda Accord", "Intermediary", -1],
    ["HIJ1237", "BMW 3 Series", "Deluxe", -1],
    ["KLM4567", "Ford Mustang", "Basic", -1],
    ["NOP7895", "Chevrolet Malibu", "Intermediary", -1],
    ["QRS0126", "Audi Q5", "Deluxe", -1],
    ["TUV3453", "Volkswagen Jetta", "Basic", -1],
    ["VWX6782", "Mercedes-Benz E-Class", "Intermediary", -1],
    ["YZA9011", "Lexus ES", "Deluxe", -1],
    ["BCD2343", "Nissan Maxima", "Basic", -1],
    ["EFG5677", "Hyundai Elantra", "Intermediary", -1],
    ["HIJ8909", "Tesla Model S", "Deluxe", -1]
    ]
    
    selected_vehicle, vehicle_index = verify_car_rent(db_vehicles)
    print(vehicle_index)
    print(selected_vehicle)

main()