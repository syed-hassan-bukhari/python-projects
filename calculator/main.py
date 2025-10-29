def add(x,y):
    return x + y 

def sub(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    if y != 0:
     return x / y
    else:
       return "Error! Division by zero."
    

print("SELECT OPERATION")
print("1. add")
print("2. subtract")
print("3. multiple")
print("4. divide")

choice = input("enter choice (1/2/3/4): ")

num1=float(input("enter first number: "))
num2=float(input("enter the second number"))


if choice == '1':
    print(f"The result is: {add(num1, num2)}")
elif choice == '2':
    print(f"The result is: {sub(num1, num2)}")
elif choice == '3':
    print(f"The result is: {multiply(num1, num2)}")
elif choice == '4':
    print(f"The result is: {divide(num1, num2)}")
else:
    print("Invalid input")