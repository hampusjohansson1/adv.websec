import base64;
from Crypto.PublicKey import RSA;

f = open('mail/keyreceiver.pem', 'r');
privateKey = RSA.importKey(f.read(),passphrase='')

msg = open("mail/mail1.msg", "r");
#print(msg.read());

mail1 = privateKey.decrypt(base64.b64decode(msg.read()));
print(mail1);