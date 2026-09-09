
print("shopping calculator")
product = input("Enter product name: ")
price = float(input("Enter product price: "))
quantity = int(input("Enter product quantity: "))
total = price * quantity
print("\n\n-------RECEIPT--------")
print(f"\n product: {product}\n price: {price}\n quantity: {quantity}\n\n\n total: {total}")