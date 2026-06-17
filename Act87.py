
s1 = {1, 2, 3, 4}
s2 = {"A", "B", "C", "D"}

s3 = list(zip(s1, s2))

print("Zipped Sets:")
print(s3)
print()

list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]

for x, y in zip(list1, list2[::-1]):
    print(x, y)

print()

stocks = ["Apple", "Google", "Microsoft", "Tesla"]
prices = [200, 150, 300, 250]

new_dict = {stock: price for stock, price in zip(stocks, prices)}

print("Stock Prices Dictionary:")
print(new_dict)