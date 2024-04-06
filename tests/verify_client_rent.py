import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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

def main():
    db_clients = [
    ['144.958.659-38', 'Joao', 'Silva', 'joao@silva.com', None],
    ['097.325.168-96', 'Maria', 'Santos', 'maria@santos.com', None],
    ['472.589.341-00', 'Pedro', 'Souza', 'pedro@souza.com', None],
    ['924.781.653-79', 'Ana', 'Oliveira', 'ana@oliveira.com', None],
    ['315.789.240-08', 'Carlos', 'Ferreira', 'carlos@ferreira.com', None],
    ['534.678.921-80', 'Juliana', 'Almeida', 'juliana@almeida.com', None],
    ['709.852.634-20', 'Lucas', 'Gomes', 'lucas@gomes.com', None],
    ['199.675.824-64', 'Mariana', 'Pereira', 'mariana@pereira.com', None],
    ['562.038.491-29', 'Fernando', 'Machado', 'fernando@machado.com', None],
    ['892.310.467-60', 'Camila', 'Costa', 'camila@costa.com', None],
    ['456.831.972-46', 'Rodrigo', 'Ribeiro', 'rodrigo@ribeiro.com', None],
    ['648.209.734-09', 'Amanda', 'Martins', 'amanda@martins.com', None],
    ['239.801.345-84', 'Mateus', 'Lima', 'mateus@lima.com', None],
    ['701.934.286-11', 'Isabela', 'Barbosa', 'isabela@barbosa.com', None],
    ['843.062.485-10', 'Gabriel', 'Fernandes', 'gabriel@fernandes.com', None],
    ['199.824.736-75', 'Laura', 'Dias', 'laura@dias.com', None],
    ['538.127.549-88', 'Larissa', 'Oliveira', 'larissa@oliveira.com', None],
    ['426.589.107-00', 'Rafael', 'Silveira', 'rafael@silveira.com', None],
    ['764.892.310-07', 'Beatriz', 'Araujo', 'beatriz@araujo.com', None],
    ['364.718.925-14', 'Vinicius', 'Rocha', 'vinicius@rocha.com', None],
    ['501.379.468-20', 'Luiza', 'Carvalho', 'luiza@carvalho.com', None],
    ['218.345.689-30', 'Eduardo', 'Cardoso', 'eduardo@cardoso.com', None],
    ['128.459.370-57', 'Natalia', 'Mendes', 'natalia@mendes.com', None],
    ['579.162.834-80', 'Gustavo', 'Farias', 'gustavo@farias.com', None],
    ['489.276.135-47', 'Carolina', 'Araujo', 'carolina@araujo.com', None],
    ['673.481.902-02', 'Matheus', 'Melo', 'matheus@melo.com', None],
    ['327.541.986-83', 'Letícia', 'Cruz', 'leticia@cruz.com', None],
    ['862.439.185-02', 'Fernanda', 'Pinto', 'fernanda@pinto.com', None],
    ['930.715.842-15', 'Roberto', 'Nunes', 'roberto@nunes.com', None],
    ['176.985.324-00', 'Bianca', 'Oliveira', 'bianca@oliveira.com', None],
    ['654.271.809-63', 'Vanessa', 'Silva', 'vanessa@silva.com', None]
    ]

    selected_client, client_index = verify_client_rent(db_clients)
    print(client_index)
    print(selected_client)
    
main()