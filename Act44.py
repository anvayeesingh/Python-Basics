row_size = int(input("Enter number of rows: "))
if row_size%2==0:
    half_diamond_row = int(row_size/2)
else:
    half_diamond_row = int(row_size/2)+1
space = half_diamond_row-1
for i in range(1, half_diamond_row+1 ):
    for j in range(1, space+1 ):
        print(end=" ")
    space = space-1
    num = 1
    for j in range(2*i-1):
        print(end=str(num))
        num = num+1
    print()
space = 1
for i in range(1,  half_diamond_row):
    for j in range(1, space+1):
        print(end=" ")
        space = space+1
        num = 1
    for j in range(1, 2*( half_diamond_row-i)):
            print(end=str(num))
            num = num+1
    print()