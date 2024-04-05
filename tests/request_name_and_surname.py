def request_name_and_surname():
    name = input("Please enter a name: ")
    surname = input("Please enter a surname: ")
    name_and_surname = [name.capitalize(), surname.capitalize()]
    
    return name_and_surname[0], name_and_surname[1]

def main():
    print(request_name_and_surname())
    
main()