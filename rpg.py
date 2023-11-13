import secrets
import string
import random


letters= string.ascii_letters
digits= string.digits
special_chars= string.punctuation
alphabet= letters+digits+special_chars

length = int(input("Enter password length: "))

pwd = ''

for i in range(length):
 
 pwd += ''.join(secrets.choice(alphabet))


print(pwd)