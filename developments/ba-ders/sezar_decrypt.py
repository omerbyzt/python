message = input("Enter encripted message : ")
password = int(input("Enter password key : "))

new_message = ""
for char in message:
    new_message += chr(ord(char)-password)

print(new_message)