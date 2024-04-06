def calculate_price(category):
    while True:
        try:
            days = int(input("How many days was the car rented? "))
        
            if category == "Basic":
                price = 150.00 * days
                return price
            elif category == "Intermediary":
                price = 250.00 * days
                return price
            else:
                price = 400.00 * days
                return price
        except ValueError:
                    print("Please enter one of the valid options.")

def main():
    print(f"R${calculate_price("Deluxe")}")

main()