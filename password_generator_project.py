import random
print('Welcome to Password Genarator')
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
 '[', ']', '{', '}', '\\', '|', ';', ':', '\'', '"', ',', '<', '.', '>', '/',
 '?', '`', '~']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

  
n_letters = int(input("How many letters would you like in your password:"))
n_symbols = int(input("How many symbols would you like in your password:"))
n_numbers = int(input("How many numbers would you like in your password:"))
password = ""
pass_list = []
final_pass = ""

for i in range(n_letters):
    char = random.choice(letters)
    password+=char

for i in range(n_symbols):
    sy = random.choice(symbols)
    password+=sy
    
for i in range(n_numbers):
    num = random.choice(numbers)
    password+=num
    
for i in range(len(password)):
    pass_list.append(password[i])  

random.shuffle(pass_list)    

for i in range(len(pass_list)):
    final = (pass_list[i])
    final_pass+=final
    
print(f"Your password is : {final_pass}") 
print("Thank you for Choosing our platform")   

    