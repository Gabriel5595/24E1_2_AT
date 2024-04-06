from components.search_vehicle_status import search_vehicle_status
from components.print_vehicle_list import print_vehicle_list

def request_vehicle_search_availability(db_vehicles):
    while True:
        try:
            print("Would you like to receive a list of available or unavailable vehicles?")
            availability = int(input("1) Available\n2) Unavailable\n"))
            
            if availability == 1:
                indexes = search_vehicle_status(db_vehicles, True)
                print_vehicle_list(db_vehicles, indexes)
                break
            elif availability == 2:
                indexes = search_vehicle_status(db_vehicles, False)
                print_vehicle_list(db_vehicles, indexes)
                break
            else:
                print("Please, enter a valid option.")
            
        except ValueError:
                    print("Please enter one of the valid options.")