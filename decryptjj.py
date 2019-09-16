#ver1.3
#reads encrypted files from folder encrypteddata, decrypts and writes output to folder decrypteddata
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import os
import base64
import bz2

def give_filenames(name):
	filenames=[]
	all_files=os.listdir('encrypteddata/')	#in python2 need to give dir: os.listdir('/home')
	
	for file in all_files:
		if name in file:
			filenames.append(file)
	return filenames


try:
	filenames=give_filenames('.encjj')
except:
	print("No file to decrypt")
	exit(0)


def ferenet_from_password(password):
	password = bytes(password.encode('utf-8'))
	salt = b'31415926538'
	kdf = PBKDF2HMAC(
		algorithm=hashes.SHA256(),
		length=32,
		salt=salt,
		iterations=100000,
		backend=default_backend()
		)
	key = base64.urlsafe_b64encode(kdf.derive(password))
	return(Fernet(key))


#default key:
fkey = Fernet(b'citj91dDrAgWQRusrotOHPb4HHE8uvT-vd8XCD43r2Q=')
#default key is replaced if another key is found in file 'secret'
for file in os.listdir():
	if file == 'secret':
		print('Using secret file...')
		with open ('secret','r') as file:
			password= file.readline().strip()
			fkey = ferenet_from_password(password)

print("Version 1.3, Jaroslaw Jankun")
print('There are {number} files to decrypt:'.format( number= str(len(filenames))) )

for filename in filenames: 
	print('Decrypting '+filename)
	
	with open ('encrypteddata/'+filename,'rb') as file:
		encrypteddata = file.read()
	
	compresseddata = fkey.decrypt(encrypteddata)
	cleardata = bz2.decompress(compresseddata)
	
	
	with open ('cleardata/'+filename[:-6],'wb') as decryptedfile:   #[:-6] to delete extension: .encjj
		decryptedfile.write(cleardata)
		
	os.remove('encrypteddata/'+filename)
