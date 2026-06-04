stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 350
}

total = 0

while True:
    stock = input("Enter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stocks:
        qty = int(input("Enter quantity: "))
        total += stocks[stock] * qty
    else:
        print("Stock not found!")

print("Total Investment Value: $", total)

with open("portfolio.txt", "w") as file:
    file.write(f"Total Investment Value: ${total}")

print("Data saved in portfolio.txt")
