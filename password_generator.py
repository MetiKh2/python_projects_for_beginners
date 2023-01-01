import secrets
import string

letters=string.ascii_letters
digits=string.digits
special_characters=string.punctuation

alphabet=letters+digits+special_characters

password_length=12

password=''

for i in range(password_length):
    password+=''.join(secrets.choice(alphabet))
    
print(password)
