#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

letters_list = []
symbols_list = []
numbers_list = []
for number in range(0,nr_letters):
    random_integer = random.randint(1, len(letters)-1)
    letters_list.append(letters[random_integer])
    
for number in range(0,nr_symbols):
    random_integer = random.randint(1, len(symbols)-1)
    symbols_list.append(symbols[random_integer])
    
for number in range(0,nr_numbers):
    random_integer = random.randint(1, len(numbers)-1)
    numbers_list.append(numbers[random_integer])
    
password = (letters_list + numbers_list + symbols_list)
random.shuffle(password)
password=''.join(password)
print(password)
    
    
    
#Note- instead of adding to a list, simply add the randomised characters to a string. eg. password = '', password += random.choice(letters)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P