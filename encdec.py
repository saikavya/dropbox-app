#Name: Sai Kavya, Dukkipati
#UTA ID:1000980778
#Course no:CSE6331
#Assignment-1
import os
import sys
import dropbox
import base64
import codecs
import gnupg
gpg = gnupg.GPG(gnupghome="C:\keys") # location for storing keys
gpg.encoding = 'UTF-8'
appkey='**********'
appsecret='********'
auth_flow = dropbox.client.DropboxOAuth2FlowNoRedirect(appkey, appsecret)
authorize_url = auth_flow.start()
print (authorize_url)
print ("2. Click allow.you might have to log in first.")
print ("3. Copy the authorization code.")
ac = input("Enter the authorization code here: ").strip()
access_token, user_id = auth_flow.finish(ac)
client = dropbox.client.DropboxClient(access_token)
print ('linked account: ', client.account_info())
#generating key
input_data = gpg.gen_key_input(key_type="RSA", key_length=1024)
print (input_data)
key = gpg.gen_key(input_data)
print (key)
#encryption
f0 = open("C:/Users/kavya dukkipati/Downloads/papa.txt", 'rb')#opening inputfile in read mode
f1= open("C:/Users/kavya dukkipati/Downloads/papa1.txt", 'w')#opening outputfile in write mode
encrypted_data = gpg.encrypt_file(f0,key,f1)#signing the file
f1.write(str(encrypted_data))# writing encrypted data to output file
f1.close()
f0.close()
#uploading
f6 = open("C:/Users/kavya dukkipati/Downloads/papa1.txt", 'rb')#opening outputfile in read mode
response = client.put_file('/enc.txt', f6)#uploading encryptedd file to dropbox
f6.close()
#download
f27, metadata = client.get_file_and_metadata('/enc.txt')# getting encrypted file from dropbox
pot = open("C:/Users/kavya dukkipati/Downloads/papa2.txt", 'wb') #opening a file in write mode to download data
pot.write(f27.read())#writing data
pot.close()
f27.close()
#decryption
d = open("C:/Users/kavya dukkipati/Downloads/papa2.txt", 'rb')# opening file in read mode
s=open("C:/Users/kavya dukkipati/Downloads/dec.txt",'w')#opening downloadedfile in write mode
decrypted_data = gpg.decrypt_file(d,key,s)# decrypting
print(decrypted_data)
s.write(str(decrypted_data))#writing decrypted data
s.close()
d.close()

