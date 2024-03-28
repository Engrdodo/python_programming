from tkinter import *
import string
import random

# PASWWORD GENERATOR (copied from day 5 project)


# This program generates a random password based on the user's input for the number of letters,
# symbols, and numbers to be included in the password. Characters can not be repeated
def generate_password():

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

    for x in range(num_letter + 1): 
        passwrd1 = random.sample(alpha_list, x)
    for y in range(num_symbol + 1):
        passwrd2 = random.sample(symbols, y)
    for z in range(num_num + 1):
        passwrd3 = random.sample(numbers, z)
    #adds the list from passwod1, passwrd2 and passwrd3 above into a single "password" below
    paswword = password.extend(passwrd1)
    paswword = password.extend(passwrd2)
    paswword = password.extend(passwrd3)
    random.shuffle(password)
    output_password = ''.join(password)
    password_entry.insert(0, output_password)



#SAVE PASSWORD

def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()


    with open("data.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)


#UI SETUP

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
#logo_img = PhotoImage(file="logo.png")
#canvas.create_image(100, 100,image=logo_img)
canvas.grid(row=0, column=1)

#labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "akinoladavidolawale@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()