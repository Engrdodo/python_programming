import string
import random

# This program generates a random password based on the user's input for the number of letters,
# symbols, and numbers to be included in the password.

lower = string.ascii_lowercase
upper = string.ascii_uppercase
alphabet = lower + upper
alpha_list = list(alphabet)
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8','9']
symbols = ['!', '#', '$', '%','&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator, Your surest plug to secure your accounts from hackers")
num_letter = int(input("How many letters would you like in your password?\n"))
num_symbol = int(input("How many symbols would you like in your password?\n"))
num_num = int(input("How many numbers would you like in your password\n"))

password = []

for x in range(1, num_letter + 1): 
    password.append(random.choice(alpha_list))
for y in range(1, num_symbol + 1):
    password.append(random.choice(symbols))
for z in range(1, num_num + 1):
    password.append(random.choice(numbers))
#adds the list from passwod1, passwrd2 and passwrd3 above into a single "password" below
# paswword = password.extend(passwrd1)
# paswword = password.extend(passwrd2)
# paswword = password.extend(passwrd3)
random.shuffle(password)
output =""
for i in password:
    output += i
print(output)



    
