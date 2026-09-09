#loops For loops
# for i in range(5):
#     print(i)

# names = ["John", "Paul", "George", "Ringo"]
# for i in names:
#     print(f"Hello {i}, this is your letter")

price = []
total = 0
for i in range(3):
    price.append(float(input("Enter price: "))) 
    
for i in price:
        total += i

print(f"total: {total}")