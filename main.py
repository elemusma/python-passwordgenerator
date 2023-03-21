#Password Generator Project
import random
from tkinter import *
import pyperclip


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '*', '+']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# print(''.join(letters))

print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))


nr_letters= random.randint(5,15)
nr_symbols = random.randint(5,15)
nr_numbers = random.randint(5,15)





#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

master_list = []

new_letters = []
length_letters = (len(letters) - 1)

for letters_range in range(0, nr_letters):
  random_letters = random.randint(0, length_letters)
  new_letters_list = letters[random_letters]
  new_letters.append(new_letters_list)
  master_list.append(new_letters_list)

# print(new_letters)

new_symbols = []
symbols_length = (len(symbols) - 1)

for symbols_range in range(0, nr_symbols):
  symbols_random = random.randint(0, symbols_length)
  new_symbols_list = symbols[symbols_random]
  new_symbols.append(new_symbols_list)
  master_list.append(new_symbols_list)

# print(new_symbols)

new_numbers = []
numbers_length = (len(numbers) - 1)

for numbers_range in range(0, nr_numbers):
  numbers_random = random.randint(0, numbers_length)
  new_numbers_list = numbers[numbers_random]
  new_numbers.append(new_numbers_list)
  master_list.append(new_numbers_list)

# print("Here is the list easy, with the letters first, symbols second and numbers third")
# print(*new_letters + new_symbols + new_numbers, sep="")


# master_list.append(new_letters)
# master_list.append(new_symbols)
# master_list.append(new_numbers)

master_list_length = len(master_list)
# print(master_list_length)

master_list_random = []
for master_characters in range(0, master_list_length):
  master_random = random.randint(0, master_list_length-1)
  master_random_character = master_list[master_random]
  master_list_random.append(master_random_character)

# print(master_list)
# print("Master list random below")
# print(*master_list_random, sep="")

print("Master list using shuffle")
random.shuffle(master_list)
# print(*master_list, sep="")
created_password = ''.join(master_list)
pyperclip.copy(created_password)
print(created_password)

window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)

quote_text = canvas.create_text(150, 207, text="Welcome to the PyPassword Generator", width=250, font=("Arial", 30, "bold"), fill="black")
quote_text = canvas.create_text(150, 285, text="The password has automatically copied to your clipboard.", width=250, font=("Arial", 15, "bold"), fill="black")
quote_text = canvas.create_text(150, 350, text=created_password, width=250, font=("Arial", 12, "bold"), fill="black")
canvas.grid(row=0, column=0)

window.mainloop()

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P