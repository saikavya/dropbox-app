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
appkey='******'
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
#signing
inputfile=input("Enter the location of the file to be signed:")
outputfile=input("Enter the location of the file to store signed message:")
f0 = open(inputfile, 'rb')#opening inputfile in read mode
f1= open(outputfile, 'w')#opening outputfile in write mode
signed_data = gpg.sign_file(f0,key,f1)#signing the file
f1.write(str(signed_data))# writing signed data to output file
f1.close()
f0.close()
#uploading
f6 = open(outputfile, 'rb')#opening outputfile in read mode
response = client.put_file('/signed.txt', f6)#uploading signed file to dropbox
f6.close()
#download
f27, metadata = client.get_file_and_metadata('/signed.txt')# getting signed file from dropbox
signeddownload=input("Enter the location of the file to download signed file:")
pot = open(signeddownload, 'wb') #opening a file in write mode to download signed data
pot.write(f27.read())#writing signed data to signeddownload file
pot.close()
f27.close()
#verification
ver=open(signeddownload, 'rb')# opening signed file in read mode
verified = gpg.verify_file(ver)# verifying the downloaded signed file
if not verified: raise ValueError("Signature could not be verified!")# error message is displayed if the signed file is not verified
print("verification")
print(str(verified))
ver.close()
#decryption
verifiedfile=input("Enter the location for storing verified and decrypted file:")
d = open(signeddownload, 'rb')# opening signed file in read mode
s=open(verifiedfile,'w')#opening verifiedfile in write mode
decrypted_data = gpg.decrypt_file(d,key,s)# decrypting the signed file
print(decrypted_data)
s.write(str(decrypted_data))#writing decrypted data to verifiedfile 
s.close()
d.close()





