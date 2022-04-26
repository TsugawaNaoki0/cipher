from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP

class decipher_class():
    def decipher(self):
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
        # print(data.decode("utf-8"))

        # ---------------------------
        # ---------------------------


        # print(type(data))

        data = data.decode("utf-8")

        # print(type(data))


        data = data.replace("+", "[\"")
        data = data.replace("*", "\"]")
        data = data.replace("@", "\", \"")

        print(data)

if __name__ == '__main__':
    aaa = decipher_class()
    bbb = aaa.decipher()
