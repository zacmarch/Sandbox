"""Zac March"""
MIN_LENGTH = 5

password = input("Enter password: ")
while len(password) < MIN_LENGTH:
    print("Password must be {} characters long".format(MIN_LENGTH))
    password = input("Enter password: ")
output = ""
for char in password:
    output += "*"
print(output)

