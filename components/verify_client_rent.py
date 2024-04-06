from components.request_cpf import request_cpf
from components.search_client_cpf import search_client_cpf

def verify_client_rent(db_clients):
    cpf = request_cpf()
    client_index = search_client_cpf(db_clients, cpf)
    
    # Verificar se o cliente realmente existe.
    # Caso o cliente exista:
    if client_index != []:
        # Verificar se cliente já tem um carro alugado.
        # Caso o cliente exista e não tenha nenhum carro alugado:
        if db_clients[client_index[0]][4] == None:
            selected_client = db_clients[client_index[0]]
            
            # Confirma se o cliente está correto
            while True:
                    try:
                        print(selected_client)
                        print("Is the client correct? If not, would you like to try again or exit?")
                        option = int(input("1) It is correct\n2) Try again.\n3) Exit.\n"))
                        
                        if option == 1:
                            return selected_client, client_index
                        elif option == 2:
                            verify_client_rent(db_clients)
                        elif option == 3:
                            selected_client = None
                            client_index = None
                            return selected_client, client_index
                        else:
                            print("The selected option is not valid.")
                        
                    except ValueError:
                        print("Please enter one of the valid options.")
        
        # Caso o cliente exista, mas já tenha um carro alugado:
        else:
            while True:
                    try:
                        print("The selected client already have a rented car. Would you like to try again or exit?")
                        option = int(input("1) Try again.\n2) Exit.\n"))
                        
                        if option == 1:
                            verify_client_rent(db_clients)
                        elif option == 2:
                            selected_client = None
                            client_index = None
                            return selected_client, client_index
                        else:
                            print("The selected option is not valid.")
                        
                    except ValueError:
                        print("Please enter one of the valid options.")
    
    # Caso o cliente não exista:
    else:
        while True:
            try:
                print("No client could be found with this CPF. Would you like to try again or exit?")
                option = int(input("1) Try again.\n2) Exit.\n"))
                
                if option == 1:
                    verify_client_rent(db_clients)
                elif option == 2:
                    selected_client = None
                    client_index = None
                    return selected_client, client_index
                else:
                    print("The selected option is not valid.")
                
            except ValueError:
                print("Please enter one of the valid options.")