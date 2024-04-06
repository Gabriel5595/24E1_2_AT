from components.search_client import search_client
from components.print_client_list import print_client_list

def request_client_search(db_clients):
    while True:
        try:
            print("Would you like search by Name or Surname?")
            name_or_surname = int(input("1) Name\n2) Surname\n"))
            
            if name_or_surname == 1:
                term = input("Please enter the name: ")
                indexes = search_client(db_clients, term, True)
                print_client_list(db_clients, indexes)
                break
            elif name_or_surname == 2:
                term = input("Please enter the surname: ")
                indexes = search_client(db_clients, term, False)
                print_client_list(db_clients, indexes)
                break
            else:
                print("Please, enter a valid option.")
            
        except ValueError:
                    print("Please enter one of the valid options.")