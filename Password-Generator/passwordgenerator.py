letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# easy level

password = ""
import random
# nr letters = 4
for char in range(0, nr_letters):
    # 1 to 4
    password += random.choice(letters)
# nr_symbols = 2
for symbol in range(1, nr_symbols + 1):
    # 1 to 2
    password += random.choice(symbols)
# nr_numbers = 3
for number in range(0, nr_numbers):
    # 1 to 3
    password += random.choice(numbers)
print(password)

# hard level

password_list = []
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))
for symbol in range(0, nr_symbols):
    password_list.append(random.choice(symbols))
for number in range(0, nr_numbers):
    password_list.append(random.choice(numbers))
print(password_list)
random.shuffle(password_list)
for each_char in password_list:
    print(each_char , end = '')
