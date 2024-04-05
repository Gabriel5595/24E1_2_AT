def verify_email(email):
    if ("@" in email):
        before_at = email.split("@")[0]
        server = email.split("@")[1]
        if (before_at.isalpha()) and ("." in server):
            return True
        else:
            return False
    else:
        return False

def main():
    email = "gabriel@hotmail.com"
    print(verify_email(email))

main()