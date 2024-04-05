def search_vehicle_status(db_vehicles, available=True):
    result = []
    
    if available:
        for index in range(len(db_vehicles)):
            if db_vehicles[index][3] == -1:
                result.append(index)
    else:
        for index in range(len(db_vehicles)):
            if db_vehicles[index][3] != -1:
                result.append(index)
    
    if result != []:
        return result
    else:
        print("No information has been found.")