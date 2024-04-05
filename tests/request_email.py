from verify_email import verify_email

def request_email():
    while True:
        email = input("Please enter a email in the format name@server.com: ")
        if verify_email(email):
            return email
        else:
            while True:
                try:
                    print("The entered email is not valid. Would you like to try again or exit?")
                    option = int(input("1) Try again.\n2) Exit.\n"))
                    
                    if option == 1:
                        request_email()
                    if option == 2:
                        break
                    else:
                        print("The selected option is not valid.")
                    break
                except ValueError:
                    print("Please enter one of the valid options.")
            return False

def main():
    print(request_email())

main()