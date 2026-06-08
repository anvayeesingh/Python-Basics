start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

squares = []
even_squares = []
odd_squares = []

for i in range(start, end + 1):
    square = i ** 2
    squares.append(square)

    if square % 2 == 0:
        even_squares.append(square)
    else:
        odd_squares.append(square)

print("Square values:", squares)
print("Even square values:", even_squares)
print("Odd square values:", odd_squares)