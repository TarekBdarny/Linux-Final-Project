import requests
import hashlib
import os
import base64
# function that hash a file in 256bites
def sha256sum(filename):
    h  = hashlib.sha256()
    b  = bytearray(128*1024)
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        while n := f.readinto(mv):
            h.update(mv[:n])
    return h.hexdigest()
# function that returns true in the string contains doe '.' else false
def find_dot(st):
    count =0
    for ch in st:
        if ch =='.': count = count+1
    return False if count==0 else True
def no_ext(st):
    return st[0 : len(st)-1-st[::-1].index('.')] if find_dot(st) else st
    
def ext(st):
    return st[len(st)-1-st[::-1].index('.'): ]

#encoding a file using base64
def encode_file(file):
    with open(file , 'rb') as f:
        encoded_bytes = base64.b64encode(f.read())
    with open(file , 'wb') as f:
        f.write(encoded_bytes)
#decoding a file using base64

def decode_file(file):
    with open(file , 'rb') as f:
        decoded_bytes = base64.b64decode(f.read())
    with open(file , 'wb') as f:
        f.write(decoded_bytes)

# function that downlaods a file , photo or song from the net
def donwlaod(url , fileName):
    res = requests.get(url , allow_redirects=True)
    new_file = no_ext(fileName) + ext(url) 
    f = open(new_file, "wb") # name of the file
    f.write(res.content)
    
