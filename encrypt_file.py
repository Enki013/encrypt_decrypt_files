import cryptography;

#Anahtar Oluşturma
from cryptography.fernet import Fernet

key=Fernet.generate_key()

with open('mykey.key','wb') as mykey:
        mykey.write(key)

        
#Anahtar Yükleme
with open('mykey.key','rb') as mykey:
    key=mykey.read()

    print(key)


# Dosyayı Şifrelemek
f=Fernet(key)
with open('grades.csv','rb') as original_file:
      original=original_file.read()

encrypted=f.encrypt(original)

with open ('enc_grades.csv','wb') as encrypted_file:
      encrypted_file.write(encrypted)

