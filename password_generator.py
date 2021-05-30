# This program is a program created by Emmanuel Olaosebikan (Dev Emmy)
# This program generates password based on users' preference
# It generates passwords greater than 6 values.

import random
import time 

input_flag=True

while input_flag:
    try:
        password_length = int(input('Password length (Greater than 5) : '))
        if password_length < 6:
            print('Password should be greater than 5')
            input_flag=True
        else:
            input_flag = False
    except:
        print('Please Input an Integer')

password_flag = True
while password_flag:
    try:
        number_of_letters = int(input('Number of letters you want in your password : '))
        if number_of_letters==password_length:
            time.sleep(2)
            number_of_digits=0
            number_of_symbols=0
            print(f'You would have { number_of_letters } letters, {number_of_digits} digits and {number_of_symbols} symbols')
            break
           
        elif number_of_letters < password_length and number_of_letters > 0:
            number_of_digits = int(input('Number of digits you want in your password : '))
            if number_of_digits < 0:
                 print('\nOut of Range, Must be higher than 0\n')
            else:
                time.sleep(2)
                if number_of_digits + number_of_letters <= password_length:
                    number_of_symbols = password_length - (number_of_letters + number_of_digits)
                    print(f'You would have { number_of_letters } letters, {number_of_digits} digits and {number_of_symbols} symbols')
                    break
                elif number_of_digits + number_of_letters > password_length:
                    print('\nOut of Range\n')

        elif number_of_letters < 0:
             print('\nOut of Range, Must be higher than 0\n')

        elif number_of_letters > password_length:
             print('\nOut of Range, Must be lesser or requal to password length\n')
         
    except:
        print("Please Input an Integer ")

lower_case_letters = 'abcdefghijklmnopqrstuvwxyz'
upper_case_letters = lower_case_letters.upper()
letters = list(lower_case_letters + upper_case_letters)
symbols = '/\!@#$%^&*|~+=_-><'
random.shuffle(letters)
digits = '0123456789'


password_letters = []
password_digits = []
password_list=[]
for i in range(number_of_letters):
    password_letters.append(random.choice(letters))


for i in range(number_of_digits):
    password_digits.append(random.choice(digits))


for i in range(number_of_symbols):
    password_digits.append(random.choice(symbols))

password_list.append(password_letters + password_digits)

password =[]
for i in range(len(password_list[0])):
    password.append(password_list[0][i])

random.shuffle(password)
generated_password = ''.join(password)
print('\nLoading...')
time.sleep(3)
print(f'\nGenerated Password :: {generated_password}')


