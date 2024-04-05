from components.verify_email import verify_email

def request_email():
    while True:
        email = input("Please enter a email in the format name@server.com: ")
        if verify_email(email):
            return email
        else:
            print("The entered email is not valid. Would you like to try again or exit?")