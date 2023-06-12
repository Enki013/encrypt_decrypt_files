import cryptography
from cryptography.fernet import Fernet
import os

# Anahtar seçeneği
key_choice = input("Anahtarı kendiniz mi belirlemek istiyorsunuz? (E/H): ")

if key_choice.upper() == 'H':
    # Anahtar Yükleme
    with open('mykey.key','rb') as mykey:
        key=mykey.read()
else:
    key = input("Lütfen anahtar metninizi girin: ").encode()
    
# Klasöre gitme ve dosya listeleme
current_directory = os.getcwd()
folder = os.path.join(current_directory, 'encrypted')
file_list = os.listdir(folder)

# Dosyaları Şifresini Çöz
f = Fernet(key)
for filename in file_list:
    with open(os.path.join(folder,filename), 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
        try: 
            decrypted = f.decrypt(encrypted)
        except cryptography.fernet.InvalidToken:
            continue
         # Dosya şifrelenmemişse pass geçmek için
        decrypted_filename = 'dec_' + filename.replace('enc_', '')
        with open(os.path.join(current_directory, 'decrypted', decrypted_filename), 'wb') as decrypted_file:
            decrypted_file.write(decrypted)

print("Bitti!")