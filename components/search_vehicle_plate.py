def search_vehicle_plate(db_vehicles, plate):
    result = []
    for index in range(len(db_vehicles)):
        if db_vehicles[index][0] == plate:
            result.append(index)
    return result