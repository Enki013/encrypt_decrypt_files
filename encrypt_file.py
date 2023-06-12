import os
from cryptography.fernet import Fernet

# Anahtar Oluşturma
key = Fernet.generate_key()

with open('mykey.key', 'wb') as mykey:
    mykey.write(key)


# Anahtar Yükleme
with open('mykey.key', 'rb') as mykey:
    key = mykey.read()

    print(key)


# Tüm Dosyaları Şifreleme


f = Fernet(key)

# Klasör yolu
current_directory = os.getcwd()
folder_path = os.path.join(current_directory, 'files')
print(folder_path)
#Dosya adlarını al
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    #Eğer .py veya .key dosyası değilse
    if not (filename.endswith('.py') or filename.endswith('.key')):

        #Dosya şifreleme
        with open(file_path, 'rb') as original_file:
            original = original_file.read()
        encrypted = f.encrypt(original)

        #Şifrelenmiş dosyaları encrypted klasörüne kaydet
        encrypted_path = os.path.join("encrypted", f'enc_{filename}')
        with open(encrypted_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

        print(f'{filename} şifrelendi.')
    else:
        print(f'{filename} şifrelenmedi.')

print('Tüm dosyalar şifrelendi.')