import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.request_name_and_surname import request_name_and_surname
from components.request_email import request_email
from components.request_cpf import request_cpf

def register_user(db_clients):
    name, surname = request_name_and_surname()
    cpf = request_cpf()
    email = request_email()
    car = None
    new_user =[]
    
    new_user = [cpf, name, surname, email, car]
    db_clients.append(new_user)
    return db_clients

def main():
    db_clients = [
    ['123.456.789-00', 'Silva', 'Joao', 'joao@silva.com', None],
    ['987.654.321-00', 'Santos', 'Maria', 'maria@santos.com', None],
    ['111.222.333-44', 'Souza', 'Pedro', 'pedro@souza.com', None],
    ['555.666.777-88', 'Oliveira', 'Ana', 'ana@oliveira.com', None],
    ['999.888.777-66', 'Ferreira', 'Carlos', 'carlos@ferreira.com', None],
    ['333.222.111-00', 'Almeida', 'Juliana', 'juliana@almeida.com', None],
    ['777.888.999-11', 'Gomes', 'Lucas', 'lucas@gomes.com', None],
    ['444.555.666-77', 'Pereira', 'Mariana', 'mariana@pereira.com', None],
    ['000.999.888-77', 'Machado', 'Fernando', 'fernando@machado.com', None],
    ['222.333.444-55', 'Costa', 'Camila', 'camila@costa.com', None],
    ['666.777.888-99', 'Ribeiro', 'Rodrigo', 'rodrigo@ribeiro.com', None],
    ['888.999.000-11', 'Martins', 'Amanda', 'amanda@martins.com', None],
    ['555.444.333-22', 'Lima', 'Mateus', 'mateus@lima.com', None],
    ['777.666.555-44', 'Barbosa', 'Isabela', 'isabela@barbosa.com', None],
    ['111.222.333-44', 'Fernandes', 'Gabriel', 'gabriel@fernandes.com', None],
    ['333.444.555-66', 'Dias', 'Laura', 'laura@dias.com', None],
    ['666.555.444-33', 'Oliveira', 'Larissa', 'larissa@oliveira.com', None],
    ['222.333.444-55', 'Silveira', 'Rafael', 'rafael@silveira.com', None],
    ['999.888.777-66', 'Araujo', 'Beatriz', 'beatriz@araujo.com', None],
    ['444.555.666-77', 'Rocha', 'Vinicius', 'vinicius@rocha.com', None],
    ['777.888.999-11', 'Carvalho', 'Luiza', 'luiza@carvalho.com', None],
    ['000.999.888-77', 'Cardoso', 'Eduardo', 'eduardo@cardoso.com', None],
    ['333.222.111-00', 'Mendes', 'Natalia', 'natalia@mendes.com', None],
    ['888.999.000-11', 'Farias', 'Gustavo', 'gustavo@farias.com', None],
    ['111.222.333-44', 'Araujo', 'Carolina', 'carolina@araujo.com', None],
    ['555.444.333-22', 'Melo', 'Matheus', 'matheus@melo.com', None],
    ['666.555.444-33', 'Cruz', 'Letícia', 'leticia@cruz.com', None],
    ['222.333.444-55', 'Pinto', 'Fernanda', 'fernanda@pinto.com', None],
    ['999.888.777-66', 'Nunes', 'Roberto', 'roberto@nunes.com', None],
    ['444.555.666-77', 'Oliveira', 'Bianca', 'bianca@oliveira.com', None],
    ['777.888.999-11', 'Silva', 'Vanessa', 'vanessa@silva.com', None]
    ]

    db_clients = register_user(db_clients)
    print(db_clients)

main()