from forex_python.converter import CurrencyRates


def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    exchange_rate = c.get_rate(from_currency, to_currency)
    converted_amount = amount * exchange_rate
    return converted_amount


from forex_python.converter import CurrencyRates, RatesNotAvailableError


def main():
    try:
        amount = float(input("Enter the amount: "))
        from_currency = input("From currency: ").upper()
        to_currency = input("To currency: ").upper()

        converted_amount = convert_currency(amount, from_currency, to_currency)
        print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
    except RatesNotAvailableError:
        print("Currency conversion rates are not available at the moment. Please try again later.")


if __name__ == "__main__":
    main()

