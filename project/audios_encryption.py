from cryptography.fernet import Fernet
import os
from pymongo import MongoClient
## Codigo com base no exemplo Fernet do crypto

def getUserKey(username):
    myclient = MongoClient("mongodb://localhost:27017/")
    mydb = myclient["biometry"]
    mycol = mydb["user_Data"]
    mydoc = mycol.find({"user": username},{"_id":0,"fernet":1})
    key = mydoc[0]["fernet"]
    return key

def FernetKey():
    key = Fernet.generate_key()
    return key

def encrypt(username,filename):
    key = getUserKey(username)
    f = Fernet(key)
    with open("./audios/"+filename+".wav", 'rb') as file:
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    with open("./audios/"+filename+".wav", 'wb') as file:
        file.write(encrypted_data)

def decrypt(username,filename):
    key = getUserKey(username)
    f = Fernet(key)
    print(filename)
    with open("./audios/"+filename+".wav", 'rb') as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    with open("./audios/"+filename+".wav", 'wb') as file:
        file.write(decrypted_data)