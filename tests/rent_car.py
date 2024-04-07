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
    ['013.394.711-40', 'Joao', 'Silva', 'joao@silva.com', None],
    ['123.456.789-00', 'Maria', 'Santos', 'maria@santos.com', "JKL0124"],
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