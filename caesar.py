#caesar cipher sederhananya adalah sebuah metode enkripsi klasik yang menggunaka metode pergeseran huruf berdasarkan sebuah kunci/key.

import string

#definition
alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
string_input_mode = input("1. Encrypt\n2. Decrypt\nMode: ")
string_result = ""

#encryption
if string_input_mode == "1":
    string_input = input("Enter your message: ")
    key = int(input("Enter your key: "))
    n = len(string_input)

    for i in range(n):
        character = string_input[i] #menentukan huruf
        location = alphabets.find(character) #mencari posisi
        new_location = (location + key) % 26 #meletakan huruf dalam posisi baru
        string_result += alphabets[new_location] #print out

    print("Encryption result: " + string_result)
    
#decryption
elif string_input_mode == "2":
    string_input = input("Enter your message: ")
    key = int(input("Enter your key: "))
    n = len(string_input)

    for i in range(n):
        character = string_input[i]
        location = alphabets.find(character)
        new_location = (location - key) % 26
        string_result += alphabets[new_location]

    print("Decryption result: " + string_result)

#references : https://www.youtube.com/watch?v=qxgeLXtd4GQ