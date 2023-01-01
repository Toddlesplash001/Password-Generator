import random
alphabets = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890,!@#$%^&*")
number = int(input("Enter number of passwords required "))
a = 0
length = int(input("Enter the length of the password "))
p = 0
for a in range(number):
    for p in range(length):
        password = (random.choice(alphabets))
        print(password, end='')
        p = p+1
    print("\n")
    a +=1


    
