"""
from cryptography.fernet import Fernet

str1 = "I am okay"
key = Fernet.generate_key()

fernet = Fernet(key)

enctex = fernet.encrypt(str1.encode())

dectex = fernet.decrypt(enctex).decode()

print("The primordial string: ", str1)
print("The Encrypted message: ", enctex)
print("The Decrypted message: ", dectex)
"""

from cryptography.fernet import Fernet

str1 = ["I am okay", "No thank you !!!", "Hello !!!"]
key = Fernet.generate_key()
token = Fernet(key)
# print(type(fernet))




class list_encrypter_class():
    def list_encrypter(self, plainList, token):
        str_list = plainList
        str_list_after = ["" for i in range(len(str_list))]
        for i in range(len(str_list)):
            enctex = token.encrypt(str_list[i].encode())
            # print("The Encrypted message: ", enctex)
            # print(enctex)
            str_list_after[i] = enctex

        return str_list_after


class list_decrypter_class():
    def list_decrypter(self, encryptedList, token):
        str_list = encryptedList

        # for k in range(len(str_list)):
        #     print(type(str_list[k]))


        str_list_after = ["" for i in range(len(str_list))]
        for i in range(len(str_list)):
            # print(type(str_list[i]))
            # dectex = token.decrypt(str_list[i].decode())
            dectex = token.decrypt(str_list[i])
            # print("The Encrypted message: ", enctex)
            # print(enctex)
            str_list_after[i] = dectex

        for k in range(len(str_list_after)):
            str_list_after[k] = str_list_after[k].decode()
        return str_list_after







hello = ["11111", "22222", "33333", "44444", "55555"]
aaa = list_encrypter_class()
bbb = aaa.list_encrypter(hello, token)
# for i in range(len(bbb)):
#     print(bbb[i])
#
# print()
# print()
# print()
# print()




ccc = list_decrypter_class()
ddd = ccc.list_decrypter(bbb, token)
# for j in range(len(ddd)):
#     print(ddd[j])
#
# for j in range(len(ddd)):
#     print(type(ddd[j]))










# print("The primordial string: ", str1)










# from Crypto.PublicKey import RSA
# from Crypto.Random import get_random_bytes
# from Crypto.Cipher import AES, PKCS1_OAEP
#
# data = "米津玄師".encode("utf-8")
# file_out = open("encrypted_data.txt", "wb")
#
# recipient_key = RSA.import_key(open("public.pem").read())
# session_key = get_random_bytes(16)
#
# # セッションキーをRSA公開鍵で暗号化する
# cipher_rsa = PKCS1_OAEP.new(recipient_key)
# enc_session_key = cipher_rsa.encrypt(session_key)
#
# # データをAESセッションキーで暗号化
# cipher_aes = AES.new(session_key, AES.MODE_EAX)
# ciphertext, tag = cipher_aes.encrypt_and_digest(data)
# [file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext)]
# file_out.close()







from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

file_in = open("encrypted_data.txt", "rb")

private_key = RSA.import_key(open("private.pem").read())

enc_session_key, nonce, tag, ciphertext = \
    [file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)]

# セッションキーをRSA秘密鍵で復号する
cipher_rsa = PKCS1_OAEP.new(private_key)
session_key = cipher_rsa.decrypt(enc_session_key)

# データをAESセッションキーで復号する
cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
data = cipher_aes.decrypt_and_verify(ciphertext, tag)
print(data.decode("utf-8"))
