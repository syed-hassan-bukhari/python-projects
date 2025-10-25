import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error fetching exchange rates. Please try again later.")
        return None
    
    data = response.json()
    rates = data["rates"]

    if to_currency.upper() not in rates:
        print("Invalid target currency!")
        return None
    
    converted_amount = amount * rates[to_currency.upper()]
    return converted_amount


def main():
    print("Welcome to the Currency Converter")

    amount = float(input("Enter amount to convert: "))
    from_currency = input("From currency (e.g., USD, EUR, PKR): ").upper()
    to_currency = input("To currency (e.g., EUR, USD, INR): ").upper()

    result = convert_currency(amount, from_currency, to_currency)

    if result:
        print(f"\{amount} {from_currency} = {result:.2f} {to_currency}")


if __name__ == "__main__":
    main()
