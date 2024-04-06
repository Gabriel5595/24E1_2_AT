import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.search_vehicle_plate import search_vehicle_plate
from components.request_plate import request_plate
from components.request_cpf import request_cpf

def rent_car(db_vehicles, db_clients):
        selected_vehicle = None
        plate = request_plate()
        
        vehicle_index = search_vehicle_plate(db_vehicles, plate)
        
        # Verifica se o o index do veículo encontrado não está vazio (Veículo encontrado)
        if vehicle_index != []:
            if db_vehicles[vehicle_index[0]][3] == -1:
                print(db_vehicles[vehicle_index[0]])
                while True:
                    try:
                        print("Is the vehicle correct? If not, would you like to try again or exit?")
                        option = int(input("1) It is correct\n2) Try again.\n3) Exit.\n"))
                        
                        if option == 1:
                            selected_vehicle = db_vehicles[vehicle_index[0]]
                        elif option == 2:
                            rent_car(db_vehicles, db_clients)
                        elif option == 3:
                            break
                        else:
                            print("The selected option is not valid.")
                        break
                    except ValueError:
                        print("Please enter one of the valid options.")
            else:
                # Dá a opção de tentar novamente ou sair
                while True:
                    try:
                        print("The selected vehicle is unavailable. Would you like to select another or exit?")
                        option = int(input("1) Try again.\n2) Exit.\n"))
                        
                        if option == 1:
                            rent_car(db_vehicles, db_clients)
                        elif option == 2:
                            break
                        else:
                            print("The selected option is not valid.")
                        break
                    except ValueError:
                        print("Please enter one of the valid options.")
        # Verifica se o o index do veículo encontrado está vazio (Veículo não encontrado)
        else:
            # Dá a opção de tentar novamente ou sair
            while True:
                try:
                    print("The entered plate is not valid. Would you like to try again or exit?")
                    option = int(input("1) Try again.\n2) Exit.\n"))
                    
                    if option == 1:
                        rent_car(db_vehicles, db_clients)
                    elif option == 2:
                        break
                    else:
                        print("The selected option is not valid.")
                    break
                except ValueError:
                    print("Please enter one of the valid options.")
        
        
        selected_client = None
        client_index = None
        cpf = request_cpf()
        
        for client in range(len(db_clients)):
            if cpf in db_clients[client][0]:
                selected_client = db_clients[client]
                client_index = [client]
        if selected_client == None:
            while True:
                try:
                    print("No client could be found with that CPF. Would you like to try again or exit?")
                    option = int(input("1) Try again.\n2) Exit.\n"))
                    
                    if option == 1:
                        rent_car(db_vehicles, db_clients)
                    elif option == 2:
                        break
                    else:
                        print("The selected option is not valid.")
                    break
                except ValueError:
                    print("Please enter one of the valid options.")
        else:
            db_vehicles[vehicle_index[0]][3] = selected_client[0]
            db_clients[client_index[0]][4] = selected_vehicle[0]
            
            print(f"Resumo da operação\nO carro {selected_vehicle[1]} de placa {selected_vehicle[0]} foi alugado pelo cliente {selected_client[1]} {selected_client[2]} de CPF {selected_client[0]} com sucesso!")
            
            return db_vehicles, db_clients
            
        
        
def main():
    db_clients = [
    ['123.456.789-00', 'Joao', 'Silva', 'joao@silva.com', "JKL0124"],
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