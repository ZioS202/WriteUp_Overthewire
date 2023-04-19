import base64
import json

key = b"KNHLKNHLKNHLKNHLKNHLKNHLKNHLKNHLKNHLKNHLKN"
new_cookie = {"showpassword":"yes", "bgcolor":"#ffffff"}
new_cookie = json.dumps(new_cookie).encode('utf-8').replace(b" ", b"")

def xor_encrypt(key, cookie):
    data = ""
    for x in range(len(key)):
        data += str(chr(cookie[x] ^ key[x % len(key)]))

    data = base64.encodebytes(data.encode('utf-8'))
    return data

data = xor_encrypt(key, new_cookie)
print(data)