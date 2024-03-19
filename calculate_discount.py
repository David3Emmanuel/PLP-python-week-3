def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = discount_percent/100 * price
        return price - discount
    else:
        return price

price = float(input("Enter original price: "))
discount_percent = float(input("Enter discount percent: "))

print("Final price after discount:", calculate_discount(price, discount_percent))
