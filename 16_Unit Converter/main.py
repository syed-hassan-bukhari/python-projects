def length_converter():
    print("\n--- Length Converter ---")
    value = float(input("Enter the value: "))
    print("Available units: meters, kilometers, centimeters, inches, feet")
    from_unit = input("Convert from: ").lower()
    to_unit = input("Convert to: ").lower()

    # Convert everything to meters first
    conversions_to_meters = {
        "meters": 1,
        "kilometers": 1000,
        "centimeters": 0.01,
        "inches": 0.0254,
        "feet": 0.3048
    }

    if from_unit not in conversions_to_meters or to_unit not in conversions_to_meters:
        print("❌ Invalid unit entered.")
        return

    value_in_meters = value * conversions_to_meters[from_unit]
    converted_value = value_in_meters / conversions_to_meters[to_unit]

    print(f"✅ {value} {from_unit} = {converted_value:.2f} {to_unit}")


def weight_converter():
    print("\n--- Weight Converter ---")
    value = float(input("Enter the value: "))
    print("Available units: grams, kilograms, pounds, ounces")
    from_unit = input("Convert from: ").lower()
    to_unit = input("Convert to: ").lower()

    # Convert everything to grams first
    conversions_to_grams = {
        "grams": 1,
        "kilograms": 1000,
        "pounds": 453.592,
        "ounces": 28.3495
    }

    if from_unit not in conversions_to_grams or to_unit not in conversions_to_grams:
        print("❌ Invalid unit entered.")
        return

    value_in_grams = value * conversions_to_grams[from_unit]
    converted_value = value_in_grams / conversions_to_grams[to_unit]

    print(f"✅ {value} {from_unit} = {converted_value:.2f} {to_unit}")


def main():
    while True:
        print("\n===== UNIT CONVERTER =====")
        print("1. Length Conversion")
        print("2. Weight Conversion")
        print("3. Exit")
        choice = input("Choose an option (1-3): ")

        if choice == "1":
            length_converter()
        elif choice == "2":
            weight_converter()
        elif choice == "3":
            print("Exiting... Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
