import itertools
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

def dec(cipher, key_length):
    msg = ""
    msg_len = float(len(cipher))
    msg_lst = list(cipher)
    col = key_length
    row = int(math.ceil(msg_len / col))
    
    dec_cipher = []
    for _ in range(row):
        dec_cipher.append([None] * col)

    for perm in itertools.permutations(range(col)):
        msg_indx = 0
        for idx in perm:
            for j in range(row):
                dec_cipher[j][idx] = msg_lst[msg_indx]
                msg_indx += 1
        
        decrypted_msg = ''.join(sum(dec_cipher, []))
        
        if decrypted_msg[:7] == "Kaliber":
            msg = decrypted_msg
            break
        
        dec_cipher = []
        for _ in range(row):
            dec_cipher.append([None] * col)
    
    return msg

msg = "Kaliber{C0lumn4l_Tr4nsp0s1t10n4l_C1ph3r}"
key = "KALIBER"
key_length = 7

cipher = enc(msg, key)
print("Encrypted flag: " + cipher)
print("Decryped flag: " + dec(cipher, key_length))
