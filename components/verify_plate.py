def verify_plate(plate):
    if len(plate) == 7:
        first_chars = plate[:3].capitalize()
        last_chars = plate[3:]
        
        if first_chars.isalpha() and last_chars.isdigit():
            return True
        else:
            return False
    else:
        return False