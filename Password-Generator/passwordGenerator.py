import os, random, datetime

os.system('cls')
os.system('clear')

# dateTime: Get date and time
date = datetime.datetime.now()

# os: Open and write to this file
file = open('passwords.txt', 'a')

# os: What characters to use when making password
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456!£$%^&*(`)"

# os: Give user input website or gmail to remember for what website password is for
website = input("Website name: ")
# os: how long you won to make your password
password_len = int(input("Length of the password: "))

for x in range(0, 1):
    password  = ""
    for x in range(0,password_len):
        password_char = random.choice(chars)
        password = password + password_char

    print(website + '\t->\t' + "Password: " + password + '\t->\t' + "Date: " + date.strftime('%d-%m-%y Time: %H:%M:%S') + '\n')
    file.write("-" * 45 + '\n')
    file.write(website + '\t->\t' + "Password: " + password + '\t->\t' + "Date: " + date.strftime('%d-%m-%y Time: %H:%M:%S') + '\n')

file.close()