def request_category():
    while True:
        try:
            print("""Please, enter the number representing one of the category options
1. Basic
2. Intermediary
3. Deluxe""")
            
            category = int(input())
            
            if category == 1:
                return "Basic"
            elif category == 2:
                return "Intermediary"
            elif category == 3:
                return "Deluxe"
            else:
                print("Number not valid. Please, enter a valid number.")
            
        except ValueError:
            print("Please, enter a valid number.")