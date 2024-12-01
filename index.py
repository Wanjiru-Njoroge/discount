def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * (discount_percent/100)
        final_price = price - discount
        return final_price
    else:
        return price


price = float(input("Enter the original price: $"))
discount = float(input("Enter the discount percentage: "))

# Calculate and display final price
final_price = calculate_discount(price, discount)

if discount >= 20:
    print(f"Final price after {discount}% discount: ${final_price:.2f}")
else:
    print(f"No discount applied. Original price: ${final_price:.2f}")