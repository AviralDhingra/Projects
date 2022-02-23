# import binascii

# from cryptography.fernet import Fernet

# key = Fernet.generate_key()
# cipher_suite = Fernet(key)

# inp = input("Text : ")

# res = ''.join(format(ord(i), '08b') for i in inp)
# # res = toBinary(inp)
# # res = ' '.join(map(bin, bytearray(inp, 'utf8')))
# # res = bin(int(binascii.hexlify(inp), 16))
# # res = bytearray(inp, "utf8")

# print(res)
# print(type(res))

# ciphered_text = cipher_suite.encrypt(res)  # required to be bytes
# print(ciphered_text)
# unciphered_text = (cipher_suite.decrypt(ciphered_text))

# print(res)
# print(type(res))

string = "Python"
binary_converted = ' '.join(map(bin, bytearray(string, "utf-8")))
print("The Binary Represntation is:", binary_converted)
print(type(binary_converted))
