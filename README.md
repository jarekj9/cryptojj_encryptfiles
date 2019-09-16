'encryptjj.py' will encrypt and delete data from folder 'cleardata', output file will be written in 'encrypteddata' folder.
'decryptjj.py' will decrypt and delete data from folder 'encrypteddata', output file will be written in 'cleardata' folder.

It also compresses data using bz2.

Text password can be specified within file: 'secret'. If that file does not exit, script will use built-in default password.

It uses Fernet symmetric encryption with 32B (byte, not bit) key.
