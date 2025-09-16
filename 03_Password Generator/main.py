import random
import string 


def generate_password(): 
 length = int(input("enter the length of password you want: "))
 lowercase = string.ascii_lowercase
 uppercase = string.ascii_uppercase
 digits = string.digits
 symbols = string.punctuation
 
 merge = lowercase + uppercase + digits + symbols 
 x = random.sample(merge,length)
 password ="".join(x)
 print(password)


while True:
    generate_password()
    again = input("\nDo you want to generate another password? (y/n): ").strip().lower()
    if again != "y":
        print("Goodbye!")
        break