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
    ['123.456.789-00', 'Joao', 'Silva', 'joao@silva.com', None],
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

    db_clients = register_user(db_clients)
    print(db_clients)

main()