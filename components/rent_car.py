def rent_car(db_vehicles, db_clients):
    selected_vehicle = None
    selected_client = None
    
    selected_vehicle, vehicle_index = verify_car_rent(db_vehicles)
    
    if (selected_vehicle != None):
        
        selected_client, client_index = verify_client_rent(db_clients)
        
        if (selected_client != None):
            
            db_vehicles[vehicle_index[0]][3] = selected_client[0]
            db_clients[client_index[0]][4] = selected_vehicle[0]
            
            print(f"Resumo da operação\nO carro {selected_vehicle[1]} de placa {selected_vehicle[0]} foi alugado pelo cliente {selected_client[1]} {selected_client[2]} de CPF {selected_client[0]} com sucesso!")
        
            return db_vehicles, db_clients
        
        else:
            return db_vehicles, db_clients
    else:
        return db_vehicles, db_clients