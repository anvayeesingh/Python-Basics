L = [4, 7, 6, 5, 1, 2, 9, 3]
print(L)

count = (0)
for i in L:
    count += i
avg = count/len(L)
print("Sum = ", count)
print("average = ", avg)
L.sort()
print(L[0])
print(L[-1])

  