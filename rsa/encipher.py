from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

class encipher_class():
    def encipher(self, data):

        data = data.encode("utf-8")

        file_out = open("encrypted_data.txt", "wb")

        recipient_key = RSA.import_key(open("public.pem").read())
        session_key = get_random_bytes(16)

        # セッションキーをRSA公開鍵で暗号化する
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        enc_session_key = cipher_rsa.encrypt(session_key)

        # データをAESセッションキーで暗号化
        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        ciphertext, tag = cipher_aes.encrypt_and_digest(data)
        [file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext)]
        file_out.close()


if __name__ == '__main__':
    data = "+お化け@おばけ@霊@幽霊@妖怪@溶解@容喙@養会@容解@ゼロ@ZERO@広角@降格@口角@高角@香格@甲殻@光角@高閣@甲賀区@白@城@Zero@無@ゴースト@亡霊@ハム@考案@公安警察@公安部@外事課@外事@障害者@ガイジ@館長@官庁@艦長@浣腸@干潮@管長@完調@間諜@攻殻機動隊@無し@なし@梨@成し@為し@作業@さ行@サ行@さぎょう@サギョウ@シロ@行動確認@zero@ZERO*"

    aaa = encipher_class()
    bbb = aaa.encipher(data)
