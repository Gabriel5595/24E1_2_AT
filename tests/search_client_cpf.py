def search_client_cpf(db_clients, cpf):
    result = []

    for index in range(len(db_clients)):
        if db_clients[index][0] == cpf:
            result.append(index)
    
    return result

def main():
    db_clients = [
    ['021.375.440-21', 'Joao', 'Silva', 'joao@silva.com', None],
    ['079.022.370-73', 'Maria', 'Santos', 'maria@santos.com', None],
    ['275.567.830-87', 'Pedro', 'Souza', 'pedro@souza.com', None],
    ['734.516.170-60', 'Ana', 'Oliveira', 'ana@oliveira.com', None],
    ['317.963.250-25', 'Carlos', 'Ferreira', 'carlos@ferreira.com', None],
    ['478.025.030-47', 'Juliana', 'Almeida', 'juliana@almeida.com', None],
    ['719.439.330-02', 'Lucas', 'Gomes', 'lucas@gomes.com', None],
    ['097.435.330-05', 'Mariana', 'Pereira', 'mariana@pereira.com', None],
    ['920.748.940-01', 'Fernando', 'Machado', 'fernando@machado.com', None],
    ['602.801.450-08', 'Camila', 'Costa', 'camila@costa.com', None],
    ['483.688.120-91', 'Rodrigo', 'Ribeiro', 'rodrigo@ribeiro.com', None],
    ['689.394.490-36', 'Amanda', 'Martins', 'amanda@martins.com', None],
    ['126.540.460-80', 'Mateus', 'Lima', 'mateus@lima.com', None],
    ['037.587.170-45', 'Isabela', 'Barbosa', 'isabela@barbosa.com', None],
    ['141.983.080-34', 'Gabriel', 'Fernandes', 'gabriel@fernandes.com', None],
    ['370.195.620-47', 'Laura', 'Dias', 'laura@dias.com', None],
    ['059.326.760-04', 'Larissa', 'Oliveira', 'larissa@oliveira.com', None],
    ['649.720.600-02', 'Rafael', 'Silveira', 'rafael@silveira.com', None],
    ['581.002.500-80', 'Beatriz', 'Araujo', 'beatriz@araujo.com', None],
    ['417.951.380-58', 'Vinicius', 'Rocha', 'vinicius@rocha.com', None],
    ['073.415.600-05', 'Luiza', 'Carvalho', 'luiza@carvalho.com', None],
    ['139.025.630-01', 'Eduardo', 'Cardoso', 'eduardo@cardoso.com', None],
    ['290.853.820-01', 'Natalia', 'Mendes', 'natalia@mendes.com', None],
    ['327.948.340-94', 'Gustavo', 'Farias', 'gustavo@farias.com', None],
    ['248.100.710-77', 'Carolina', 'Araujo', 'carolina@araujo.com', None],
    ['647.068.230-33', 'Matheus', 'Melo', 'matheus@melo.com', None],
    ['948.326.980-19', 'Letícia', 'Cruz', 'leticia@cruz.com', None],
    ['520.471.760-48', 'Fernanda', 'Pinto', 'fernanda@pinto.com', None],
    ['774.569.180-98', 'Roberto', 'Nunes', 'roberto@nunes.com', None],
    ['829.607.680-08', 'Bianca', 'Oliveira', 'bianca@oliveira.com', None],
    ['095.746.510-49', 'Vanessa', 'Silva', 'vanessa@silva.com', None]
    ]

    
    print(search_client_cpf(db_clients, '059.326.760-04'))

main()