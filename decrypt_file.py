import cryptography
from cryptography.fernet import Fernet

key_choice = input("Anahtarı kendiniz mi belirlemek istiyorsunuz? (E/H): ")

if key_choice.upper() == 'H':
    # Anahtar Yükleme
    with open('mykey.key','rb') as mykey:
        key=mykey.read()
else:
    key = input("Lütfen anahtar metninizi girin: ").encode()

# Dosyanın Şifresini Çözme
f = Fernet(key)
with open('enc_grades.csv', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

    decrypted = f.decrypt(encrypted)

    with open('dec_grades.csv', 'wb') as decrypterd_file:
        decrypterd_file.write(decrypted)
