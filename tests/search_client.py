def search_client(db_clients, term, name_or_surname=True):
    result = []
    
    if name_or_surname:
        for index in range(len(db_clients)):
            if db_clients[index][1] == term:
                result.append(index)
        return result
    else:
        for index in range(len(db_clients)):
            if db_clients[index][2] == term:
                result.append(index)
        return result

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
    
    print(search_client(db_clients, "Fernanda", True))

main()