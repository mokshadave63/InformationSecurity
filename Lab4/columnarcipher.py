import math

key="HACK"

def encryptMessage(msg):
    cipher=""
    k_index=0
    msg_len=float(len(msg))
    msg_list=list(msg)
    key_list=sorted(list(key))

    col=len(key)
    row=int(math.ceil(msg_len/col))

    fill_null=int((row*col)-msg_len)
    msg_list.extend('_'*fill_null)

    matrix=[msg_list[i:i+col]
            for i in range(0, len(msg_list), col)]
    
    for _ in range(col):
        curr_idx=key.index(key_list[k_index])
        cipher+= ''.join([row[curr_idx]
                          for row in matrix])
        k_index+=1
    return cipher

def decryptMessage(cipher):
    msg=""
    k_index=0
    msg_index=0
    msg_len=float(len(cipher))
    msg_list=list(cipher)

    col=len(key)
    row=int(math.ceil(msg_len/col))