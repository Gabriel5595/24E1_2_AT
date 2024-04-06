def fleet_menu():
    while True:
        try:
            print("\n***FLEET MANAGEMENT***")
            print("Please, select one of the options below")
            option = int(input("1) Register Vehicle.\n2) Search by Plate.\n3) Search by Availability.\n4) Return to Previous Menu"))
            
            if option == 1:
                pass
            elif option == 2:
                pass
            elif option == 3:
                pass
            elif option == 4:
                pass
            else:
                print("The selected option is not valid.")
        except ValueError:
                    print("Please enter one of the valid options.")

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
    fleet_menu()

main()