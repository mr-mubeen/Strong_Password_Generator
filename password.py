import os, random, string

length = 10
print("*********************************************************")
name = input("Enter a word that you want to use for password \n" )
print("*********************************************************")
TO_GENERATE = int(input("How many passwords you have to create:- \n"))
print("*********************************************************")
print("Below are your strong password generated using  : " + name)
print("*********************************************************")

for passw in range(TO_GENERATE):
    
    chars = string.ascii_letters + string.digits + '!@#$%^&*()'
    random.seed = (os.urandom(1024))

    a = (''.join(random.choice(chars) for i in range(length)))
    print(name + "!"+ a)