
def invest(amount, rate, years):
    for i in range(years):
        amount = amount + (amount * rate)
        print(f"Year {i+1}: ${amount:.2f}")

user_input = input("Enter the amount of money to invest: ")
amount = float(user_input)

user_input = input("Enter the annual interest rate: ")
rate = float(user_input)

user_input = input("Enter the number of years: ")
years = int(user_input)

invest(amount, rate, years)