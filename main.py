from components.main_menu import main_menu

def main():
    db_clients = [
    ['738.341.011-41', 'Joao', 'Silva', 'joao@silva.com', None],
    ['642.664.531-16', 'Maria', 'Santos', 'maria@santos.com', None],
    ['766.457.362-90', 'Pedro', 'Souza', 'pedro@souza.com', None],
    ['374.286.461-03', 'Ana', 'Oliveira', 'ana@oliveira.com', None],
    ['720.101.999-60', 'Carlos', 'Ferreira', 'carlos@ferreira.com', None],
    ['711.214.489-25', 'Juliana', 'Almeida', 'juliana@almeida.com', None],
    ['639.980.021-89', 'Lucas', 'Gomes', 'lucas@gomes.com', None],
    ['576.777.685-71', 'Mariana', 'Pereira', 'mariana@pereira.com', None],
    ['213.173.053-53', 'Fernando', 'Machado', 'fernando@machado.com', None],
    ['708.539.533-84', 'Camila', 'Costa', 'camila@costa.com', None],
    ['690.314.857-48', 'Rodrigo', 'Ribeiro', 'rodrigo@ribeiro.com', None],
    ['091.315.355-93', 'Amanda', 'Martins', 'amanda@martins.com', None],
    ['113.177.922-38', 'Mateus', 'Lima', 'mateus@lima.com', None],
    ['984.986.913-54', 'Isabela', 'Barbosa', 'isabela@barbosa.com', None],
    ['384.824.569-89', 'Gabriel', 'Fernandes', 'gabriel@fernandes.com', None],
    ['428.857.979-16', 'Laura', 'Dias', 'laura@dias.com', None],
    ['299.872.637-20', 'Larissa', 'Oliveira', 'larissa@oliveira.com', None],
    ['454.637.427-58', 'Rafael', 'Silveira', 'rafael@silveira.com', None],
    ['864.937.807-21', 'Beatriz', 'Araujo', 'beatriz@araujo.com', None],
    ['547.799.250-61', 'Vinicius', 'Rocha', 'vinicius@rocha.com', None],
    ['298.904.936-32', 'Luiza', 'Carvalho', 'luiza@carvalho.com', None],
    ['526.685.220-80', 'Eduardo', 'Cardoso', 'eduardo@cardoso.com', None],
    ['100.547.068-58', 'Natalia', 'Mendes', 'natalia@mendes.com', None],
    ['919.376.707-24', 'Gustavo', 'Farias', 'gustavo@farias.com', None],
    ['790.434.974-44', 'Carolina', 'Araujo', 'carolina@araujo.com', None],
    ['536.409.214-37', 'Matheus', 'Melo', 'matheus@melo.com', None],
    ['368.627.374-81', 'Letícia', 'Cruz', 'leticia@cruz.com', None],
    ['306.347.964-02', 'Fernanda', 'Pinto', 'fernanda@pinto.com', None],
    ['322.836.161-66', 'Roberto', 'Nunes', 'roberto@nunes.com', None],
    ['713.384.161-46', 'Bianca', 'Oliveira', 'bianca@oliveira.com', None],
    ['212.121.571-92', 'Vanessa', 'Silva', 'vanessa@silva.com', None],
]
    db_vehicles = [
    ["JKL0124", "Ford Focus", "Basic", -1],
    ["MNO3455", "Chevrolet Cruze", "Intermediary", -1],
    ["PQR6786", "Audi A4", "Deluxe", -1],
    ["STU9012", "Volkswagen Golf", "Basic", -1],
    ["VWX2347", "Mercedes-Benz C-Class", "Intermediary", -1],
    ["YZA5678", "Lexus RX", "Deluxe", -1],
    ["BCD8903", "Nissan Altima", "Basic", -1],
    ["EFG1231", "Hyundai Sonata", "Intermediary", -1],
    ["HIJ4564", "Tesla Model 3", "Deluxe", -1],
    ["KLM7895", "Subaru Outback", "Basic", -1],
    ["NOP0123", "Kia Optima", "Intermediary", -1],
    ["QRS3450", "Volvo XC90", "Deluxe", -1],
    ["TUV6787", "Mazda CX-5", "Basic", -1],
    ["VWX9015", "Land Rover Range Rover", "Intermediary", -1],
    ["YZA2346", "Jeep Wrangler", "Deluxe", -1],
    ["BCD5677", "Toyota Camry", "Basic", -1],
    ["EFG8908", "Honda Accord", "Intermediary", -1],
    ["HIJ1237", "BMW 3 Series", "Deluxe", -1],
    ["KLM4567", "Ford Mustang", "Basic", -1],
    ["NOP7895", "Chevrolet Malibu", "Intermediary", -1],
    ["QRS0126", "Audi Q5", "Deluxe", -1],
    ["TUV3453", "Volkswagen Jetta", "Basic", -1],
    ["VWX6782", "Mercedes-Benz E-Class", "Intermediary", -1],
    ["YZA9011", "Lexus ES", "Deluxe", -1],
    ["BCD2343", "Nissan Maxima", "Basic", -1],
    ["EFG5677", "Hyundai Elantra", "Intermediary", -1],
    ["HIJ8909", "Tesla Model S", "Deluxe", -1]
]
    
    main_menu(db_vehicles, db_clients)

main()