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

def main():
    db_vehicles = [
    ["JKL012", "Ford Focus", "Basic", -1],
    ["MNO345", "Chevrolet Cruze", "Intermediary", -1],
    ["PQR678", "Audi A4", "Deluxe", -1],
    ["STU901", "Volkswagen Golf", "Basic", -1],
    ["VWX234", "Mercedes-Benz C-Class", "Intermediary", -1],
    ["YZA567", "Lexus RX", "Deluxe", -1],
    ["BCD890", "Nissan Altima", "Basic", -1],
    ["EFG123", "Hyundai Sonata", "Intermediary", -1],
    ["HIJ456", "Tesla Model 3", "Deluxe", -1],
    ["KLM789", "Subaru Outback", "Basic", -1],
    ["NOP012", "Kia Optima", "Intermediary", -1],
    ["QRS345", "Volvo XC90", "Deluxe", -1],
    ["TUV678", "Mazda CX-5", "Basic", -1],
    ["VWX901", "Land Rover Range Rover", "Intermediary", -1],
    ["YZA234", "Jeep Wrangler", "Deluxe", -1],
    ["BCD567", "Toyota Camry", "Basic", -1],
    ["EFG890", "Honda Accord", "Intermediary", -1],
    ["HIJ123", "BMW 3 Series", "Deluxe", -1],
    ["KLM456", "Ford Mustang", "Basic", -1],
    ["NOP789", "Chevrolet Malibu", "Intermediary", -1],
    ["QRS012", "Audi Q5", "Deluxe", -1],
    ["TUV345", "Volkswagen Jetta", "Basic", -1],
    ["VWX678", "Mercedes-Benz E-Class", "Intermediary", -1],
    ["YZA901", "Lexus ES", "Deluxe", -1],
    ["BCD234", "Nissan Maxima", "Basic", -1],
    ["EFG567", "Hyundai Elantra", "Intermediary", -1],
    ["HIJ890", "Tesla Model S", "Deluxe", -1]
]
    print(search_vehicle_status(db_vehicles, available=False))

main()