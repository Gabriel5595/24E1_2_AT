import sys
import os
# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from components.verify_plate import verify_plate

def request_plate():
    while True:
        plate = input("Please enter the plate of the vehicle (ABC1234): ")
        
        if verify_plate(plate):
            return plate
        else:
            print("The plate entered is not valid. Please enter a plate with 3 letters and 4 numbers.")

def main():
    print(request_plate())

main()