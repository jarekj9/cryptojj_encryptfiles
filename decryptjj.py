#ver1.2
#reads encrypted files from folder encrypteddata, decrypts and writes output to folder decrypteddata
from cryptography.fernet import Fernet
import os

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


fkey = Fernet(b'citj91dDrAgWQRusrotOHPb4HHE8uvT-vd8XCD43r2Q=')

print("Version 1.2, Jaroslaw Jankun")
print('There are {number} files to decrypt:'.format( number= str(len(filenames))) )

for filename in filenames: 
	print('Decrypting '+filename)
	
	with open ('encrypteddata/'+filename,'rb') as file:
		encrypteddata=file.read()
	
	with open ('cleardata/'+filename[:-6],'wb') as decryptedfile:   #[:-6] to delete extension: .encjj
		decryptedfile.write(fkey.decrypt(encrypteddata))
		
	os.remove('encrypteddata/'+filename)
