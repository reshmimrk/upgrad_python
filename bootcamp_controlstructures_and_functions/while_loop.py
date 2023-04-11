import sys
pin = input("Enter the pin: ")

attempt_count = 1
while pin != '1234':
    print(attempt_count)
    if attempt_count >= 3:
     sys.exit("Too many invalid attempts")   #error code
    pin = input('Invalid input, please try again: ')  
    attempt_count += 1
print("Pin validation successful.")