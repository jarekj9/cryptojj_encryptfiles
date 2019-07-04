#ver1.2
#encrypts all files in folder cleardata and writes output files to encrypteddata folder

from cryptography.fernet import Fernet
import os

def give_filenames(name):
	filenames=[]
	all_files=os.listdir('cleardata/')	#in python2 need to give dir: os.listdir('/home')
	
	for file in all_files:
		if name in file:
			filenames.append(file)
	return filenames


try:
	filenames=give_filenames('')
except:
	print("No file to encrypt")
	exit(0)


fkey = Fernet(b'citj91dDrAgWQRusrotOHPb4HHE8uvT-vd8XCD43r2Q=')

print("Version 1.2, Jaroslaw Jankun")
print('There are {number} files to encrypt:'.format( number= str(len(filenames))) )

for filename in filenames: 
	print('Encrypting '+filename)
	
	with open ('cleardata/'+filename,'rb') as file:
		cleardata=file.read()

	with open ('encrypteddata/'+filename+'.encjj','wb') as encryptedfile:
		encryptedfile.write(fkey.encrypt(cleardata))
		
	os.remove('cleardata/'+filename)
