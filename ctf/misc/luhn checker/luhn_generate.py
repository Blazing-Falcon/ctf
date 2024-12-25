import random

def gen(length=16):
    digits = [random.randint(0, 9) for _ in range(length - 1)]
    total = 0
    for i, digit in enumerate(reversed(digits)):
        n = digit
        if i % 2 == 0:  
            n *= 2
            if n > 9:  
                n -= 9
        total += n
    check_digit = (10 - (total % 10)) % 10
    digits.append(check_digit)
    return ''.join(map(str, digits))

code = gen(16)
print(code)
