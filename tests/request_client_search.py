import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

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

def main():
    db_clients = [
    ['013.394.711-40', 'Joao', 'Silva', 'joao@silva.com', "JKL0124"],
    ['987.654.321-00', 'Maria', 'Santos', 'maria@santos.com', None],
    ['111.222.333-44', 'Pedro', 'Souza', 'pedro@souza.com', None],
    ['555.666.777-88', 'Ana', 'Oliveira', 'ana@oliveira.com', None],
    ['999.888.777-66', 'Carlos', 'Ferreira', 'carlos@ferreira.com', None],
    ['333.222.111-00', 'Juliana', 'Almeida', 'juliana@almeida.com', None],
    ['777.888.999-11', 'Lucas', 'Gomes', 'lucas@gomes.com', None],
    ['444.555.666-77', 'Mariana', 'Pereira', 'mariana@pereira.com', None],
    ['000.999.888-77', 'Fernando', 'Machado', 'fernando@machado.com', None],
    ['222.333.444-55', 'Camila', 'Costa', 'camila@costa.com', None],
    ['666.777.888-99', 'Rodrigo', 'Ribeiro', 'rodrigo@ribeiro.com', None],
    ['888.999.000-11', 'Amanda', 'Martins', 'amanda@martins.com', None],
    ['555.444.333-22', 'Mateus', 'Lima', 'mateus@lima.com', None],
    ['777.666.555-44', 'Isabela', 'Barbosa', 'isabela@barbosa.com', None],
    ['111.222.333-44', 'Gabriel', 'Fernandes', 'gabriel@fernandes.com', None],
    ['333.444.555-66', 'Laura', 'Dias', 'laura@dias.com', None],
    ['666.555.444-33', 'Larissa', 'Oliveira', 'larissa@oliveira.com', None],
    ['222.333.444-55', 'Rafael', 'Silveira', 'rafael@silveira.com', None],
    ['999.888.777-66', 'Beatriz', 'Araujo', 'beatriz@araujo.com', None],
    ['444.555.666-77', 'Vinicius', 'Rocha', 'vinicius@rocha.com', None],
    ['777.888.999-11', 'Luiza', 'Carvalho', 'luiza@carvalho.com', None],
    ['000.999.888-77', 'Eduardo', 'Cardoso', 'eduardo@cardoso.com', None],
    ['333.222.111-00', 'Natalia', 'Mendes', 'natalia@mendes.com', None],
    ['888.999.000-11', 'Gustavo', 'Farias', 'gustavo@farias.com', None],
    ['111.222.333-44', 'Carolina', 'Araujo', 'carolina@araujo.com', None],
    ['555.444.333-22', 'Matheus', 'Melo', 'matheus@melo.com', None],
    ['666.555.444-33', 'Letícia', 'Cruz', 'leticia@cruz.com', None],
    ['222.333.444-55', 'Fernanda', 'Pinto', 'fernanda@pinto.com', None],
    ['999.888.777-66', 'Roberto', 'Nunes', 'roberto@nunes.com', None],
    ['444.555.666-77', 'Bianca', 'Oliveira', 'bianca@oliveira.com', None],
    ['777.888.999-11', 'Vanessa', 'Silva', 'vanessa@silva.com', None]
    ]
    request_client_search(db_clients)

main()