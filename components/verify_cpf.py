def verify_cpf(cpf):
    if len(cpf) != 11:
        return False
    
    digits = [int(d) for d in cpf]
    multipliers1 = list(range(10, 1, -1))
    multipliers2 = list(range(11, 1, -1))
    
    sum1 = sum(d * m1 for d, m1 in zip(digits[:9], multipliers1))
    rest1 = sum1 % 11
    verifyingDigit1 = 11 - rest1 if rest1 >= 2 else 0
    
    sum2 = sum(d * m2 for d, m2 in zip(digits[:10], multipliers2))
    rest2 = sum2 % 11
    verifyingDigit2 = 11 - rest2 if rest2 >= 2 else 0
    
    return digits[9] == verifyingDigit1 and digits[10] == verifyingDigit2