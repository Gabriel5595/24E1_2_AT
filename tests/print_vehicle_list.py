def print_vehicle_list(db_vehicles, indexes):
    for index in range(len(indexes)):
        print(db_vehicles[indexes[index]])

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
    print_vehicle_list(db_vehicles, [0, 3, 5, 26])

main()