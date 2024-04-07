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
    ['174.444.283-52', 'Joao', 'Silva', 'joao@silva.com', None]
    ['080.524.161-24', 'Maria', 'Santos', 'maria@santos.com', None]
    ['043.713.499-78', 'Pedro', 'Souza', 'pedro@souza.com', None]
    ['229.230.332-99', 'Ana', 'Oliveira', 'ana@oliveira.com', None]
    ['956.904.950-26', 'Carlos', 'Ferreira', 'carlos@ferreira.com', None]
    ['407.819.248-39', 'Juliana', 'Almeida', 'juliana@almeida.com', None]
    ['160.302.077-25', 'Lucas', 'Gomes', 'lucas@gomes.com', None]
    ['284.877.191-71', 'Mariana', 'Pereira', 'mariana@pereira.com', None]
    ['633.851.771-03', 'Fernando', 'Machado', 'fernando@machado.com', None]
    ['625.754.113-19', 'Camila', 'Costa', 'camila@costa.com', None]
    ['301.148.271-33', 'Rodrigo', 'Ribeiro', 'rodrigo@ribeiro.com', None]
    ['384.718.888-74', 'Amanda', 'Martins', 'amanda@martins.com', None]
    ['237.252.060-15', 'Mateus', 'Lima', 'mateus@lima.com', None]
    ['876.876.661-00', 'Isabela', 'Barbosa', 'isabela@barbosa.com', None]
    ['383.288.562-55', 'Gabriel', 'Fernandes', 'gabriel@fernandes.com', None]
    ['149.641.857-37', 'Laura', 'Dias', 'laura@dias.com', None]
    ['606.619.076-86', 'Larissa', 'Oliveira', 'larissa@oliveira.com', None]
    ['745.084.623-32', 'Rafael', 'Silveira', 'rafael@silveira.com', None]
    ['140.269.547-06', 'Beatriz', 'Araujo', 'beatriz@araujo.com', None]
    ['578.619.742-51', 'Vinicius', 'Rocha', 'vinicius@rocha.com', None]
    ['245.548.981-72', 'Luiza', 'Carvalho', 'luiza@carvalho.com', None]
    ['337.272.634-07', 'Eduardo', 'Cardoso', 'eduardo@cardoso.com', None]
    ['858.080.774-35', 'Natalia', 'Mendes', 'natalia@mendes.com', None]
    ['603.716.674-96', 'Gustavo', 'Farias', 'gustavo@farias.com', None]
    ['195.457.947-04', 'Carolina', 'Araujo', 'carolina@araujo.com', None]
    ['667.342.873-27', 'Matheus', 'Melo', 'matheus@melo.com', None]
    ['532.933.496-92', 'Letícia', 'Cruz', 'leticia@cruz.com', None]
    ['925.997.686-32', 'Fernanda', 'Pinto', 'fernanda@pinto.com', None]
    ['719.066.401-73', 'Roberto', 'Nunes', 'roberto@nunes.com', None]
    ['481.432.199-68', 'Bianca', 'Oliveira', 'bianca@oliveira.com', None]
    ['624.357.141-65', 'Vanessa', 'Silva', 'vanessa@silva.com', None]
]

    selected_client, client_index = verify_client_rent(db_clients)
    print(client_index)
    print(selected_client)
    
main()