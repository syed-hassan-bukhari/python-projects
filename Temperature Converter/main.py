def celsius_to_fahrenheit(c):
    return ( c  *  9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32 ) * 5/9

def main():
    while True:
        print(" TEMPRATURE CONVERTOR  ")
        print("1. celsius to fahrenhiet ")
        print("2. fahrehiet to celsius ")
        print("3. EXIT ")


        choice = input("choose an option (1/2/3): ") 

        if choice == "1":
            c=float(input("enter temprature in celsius: "))
            print(f"{c}°C = {celsius_to_fahrenheit(c):.2f}°F")
        elif choice== "2":
            f=float(input("enter temprature in fahrenhiet: ")) 
            print(f"{f}°F = {fahrenheit_to_celsius(f):.2f}°C")      
        elif choice== "3":
            print("GOOD BYE!")
            break    
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    main() 