import math

def enc(flag, key):
    cipher = ""
    k_idx = 0
    flag_len = float(len(flag))
    flag_lst = list(flag)
    key_lst = sorted(list(key))
    col = len(key)
    row = int(math.ceil(flag_len / col))
    
    fill_null = int((row * col) - flag_len)
    flag_lst.extend('-' * fill_null)
    
    matrix = [flag_lst[i: i + col] for i in range(0, len(flag_lst), col)]
    
    for x in range(col):
        curr_idx = key.index(key_lst[k_idx])
        cipher += ''.join([row[curr_idx]
                           for row in matrix])
        k_idx += 1
        
    return cipher

def dec():
    return 0

msg = "Kaliber{C0lumn4l_Tr4nsp0s1t10n4l_C1ph3r}"
key = "" #key menghilang
key_length = 7

cipher = enc(msg, key)
print("Encrypted flag: " + cipher)
print("Decryped flag: ")
