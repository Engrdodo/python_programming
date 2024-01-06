import string
import random


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

for x in range(num_letter + 1): #and (symb in range(num_symbol + 1)) and (num in range(num_num + 1)):
    passwrd1 = random.sample(alpha_list, x)
    #password.ape
for y in range(num_symbol + 1):
    passwrd2 = random.sample(symbols, y)
for z in range(num_num + 1):
    passwrd3 = random.sample(numbers, z)
paswword = password.extend(passwrd1)
paswword = password.extend(passwrd2)
paswword = password.extend(passwrd3)
random.shuffle(password)
for items in password:
    str(items)
    print(items, end = '')
print()




    
