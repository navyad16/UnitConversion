#Built a robust Python-based unit converter supporting length, weight, temperature, time, and live currency conversion using ExchangeRate API.

import requests

def convert_length(value, from_unit, to_unit):
    units = {"m": 1, "km": 1000, "mi": 1609.34, "ft": 0.3048}
    return value * units[from_unit] / units[to_unit]

def convert_weight(value, from_unit, to_unit):
    units = {"g": 1, "kg": 1000, "lb": 453.592, "oz": 28.3495}
    return value * units[from_unit] / units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    from_unit, to_unit = from_unit.upper(), to_unit.upper()
    if from_unit == to_unit: return value
    if from_unit == "C": return (value * 9/5) + 32 if to_unit == "F" else value + 273.15
    if from_unit == "F": return (value - 32) * 5/9 if to_unit == "C" else (value - 32) * 5/9 + 273.15
    if from_unit == "K": return value - 273.15 if to_unit == "C" else (value - 273.15) * 9/5 + 32
    raise ValueError("Invalid temperature units.")

def convert_time(value, from_unit, to_unit):
    units = {"s": 1, "min": 60, "h": 3600}
    return value * units[from_unit] / units[to_unit]

def convert_currency(value, from_currency, to_currency):
    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"
        response = requests.get(url)
        data = response.json()
        rate = data['rates'].get(to_currency.upper())
        if rate:
            return value * rate
        else:
            raise ValueError("Invalid currency code.")
    except Exception:
        raise ValueError("Currency conversion failed. Check internet/API.")

def main():
    print("\n🔁 Multi Unit Converter")
    print("Categories:\n1. Length\n2. Weight\n3. Temperature\n4. Time\n5. Currency")
    choice = input("Enter choice (1–5): ").strip()

    try:
        value = float(input("Enter value to convert: "))
        from_unit = input("From unit/code: ").strip().lower()
        to_unit = input("To unit/code: ").strip().lower()

        if choice == "1":
            result = convert_length(value, from_unit, to_unit)
        elif choice == "2":
            result = convert_weight(value, from_unit, to_unit)
        elif choice == "3":
            result = convert_temperature(value, from_unit, to_unit)
        elif choice == "4":
            result = convert_time(value, from_unit, to_unit)
        elif choice == "5":
            result = convert_currency(value, from_unit, to_unit)
        else:
            print("❌ Invalid category choice.")
            return

        print(f"\n✅ {value} {from_unit} = {round(result, 4)} {to_unit}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()

