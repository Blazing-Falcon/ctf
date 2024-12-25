def luhn_check(kode):
    total = 0
    reversed = kode[::-1]    
    if len(kode) != 16:
        return
    for i, digit in enumerate(reversed):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9   
        total += n
    return total % 10 == 0

kode = input("masukkan kode untuk dicheck (16 angka): ")
if luhn_check(kode) == True:
    print("kode valid")
    print("here's ur flag:")
    try:
        with open("flag.txt", "r") as file:
            print(file.read().strip())
    except FileNotFoundError:
        print("Flag not found!")
else:
    print("kode invalid")