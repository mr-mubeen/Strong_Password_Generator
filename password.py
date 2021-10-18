import os, random, string

length = 3
print("*********************************************************")
name = input("Enter a word that you want to use for password \n" )
print("*********************************************************")
TO_GENERATE = int(input("How many passwords you have to create:- \n"))
print("*********************************************************")
print("Below are your strong password generated using  : " + name)
print("*********************************************************")

for passw in range(TO_GENERATE):
    
    chars = string.ascii_letters
    digits =  string.digits 
    sp = '!@#$%^&*()'

    a = (''.join(random.choice(chars) + ''.join(random.choice(digits) + ''.join(random.choice(sp))) for i in range(length)))
    print(name + a)
