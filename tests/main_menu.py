def main_menu():
    while True:
        try:
            print("\n***MAIN MANAGEMENT***")
            print("Please, select one of the options below")
            option = int(input("1) Fleet Management.\n2) Clients Management.\n3) Rents Management.\n4) Exit"))
            
            if option == 1:
                pass
            elif option == 2:
                pass
            elif option == 3:
                pass
            elif option == 4:
                break
            else:
                print("The selected option is not valid.")
            break
        except ValueError:
                    print("Please enter one of the valid options.")

def main():
    main_menu()

main()