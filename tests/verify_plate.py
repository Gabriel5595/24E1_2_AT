def verify_plate(plate):
    if len(plate) == 7:
        first_chars = plate[:3].capitalize()
        last_chars = plate[3:]
        
        #if all(char.isalpha() for char in first_chars) and all(char.isdigit() for char in last_chars):
        if first_chars.isalpha() and last_chars.isdigit():
            return True
        else:
            return False
    else:
        return False

def main():
    print(verify_plate("ABC1234"))
    

main()