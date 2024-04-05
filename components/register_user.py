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