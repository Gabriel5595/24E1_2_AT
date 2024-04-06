from components.verify_cpf import verify_cpf
from components.format_cpf import format_cpf

def request_cpf():
    while True:
        try:
            cpf = input("Please, enter only the 11 CPF numbers: ")
            
            if verify_cpf(cpf):
                return format_cpf(cpf)
            else:
                print("The CPF entered is not valid. Please enter another.")
            
        except ValueError:
            print("Please, enter a CPF composed of 11 numbers.")