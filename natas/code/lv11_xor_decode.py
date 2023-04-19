import base64
import json

ciphertext = b"MGw7JCQ5OC04PT8jOSpqdmkgJ25nbCorKCEkIzlscm5oKC4qLSgubjY="
ciphertext = base64.decodebytes(ciphertext)
plaintext = {"showpassword":"no", "bgcolor":"#ffffff"}
#xóa khoảng trắng vì json python khác php 
plaintext = json.dumps(plaintext).encode('utf-8').replace(b" ", b"")

def xor_decrypt(plaintext, ciphertext):
    key = ""
    for i in range(len(plaintext)):
        key += str(chr(ciphertext[i] ^ plaintext[i % len(plaintext)]))
    return key

key = xor_decrypt(ciphertext, plaintext)
print(key)