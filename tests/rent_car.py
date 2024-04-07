import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.verify_client_rent import verify_client_rent
from components.verify_car_rent import verify_car_rent

def rent_car(db_vehicles, db_clients):
    selected_vehicle = None
    selected_client = None
    
    selected_vehicle, vehicle_index = verify_car_rent(db_vehicles)
    
    if (selected_vehicle != None):
        
        selected_client, client_index = verify_client_rent(db_clients)
        
        if (selected_client != None):
            
            db_vehicles[vehicle_index[0]][3] = selected_client[0]
            db_clients[client_index[0]][4] = selected_vehicle[0]
            
            print(f"Resumo da operação\nO carro {selected_vehicle[1]} de placa {selected_vehicle[0]} foi alugado pelo cliente {selected_client[1]} {selected_client[2]} de CPF {selected_client[0]} com sucesso!")
        
            return db_vehicles, db_clients
        
        else:
            return db_vehicles, db_clients
    else:
        return db_vehicles, db_clients

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
    
    db_vehicles = [
    ["JKL0124", "Ford Focus", "Basic", '123.456.789-00'],
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
    
    rent_car(db_vehicles, db_clients)

main()