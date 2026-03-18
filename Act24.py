
print("Enter a number (Numerator): ")
num = int(input())
print("Enter a number (Denominator)")
numn = int(input())

if num%numn==0:
    print("\n" +str(num)+ "is divisible by "+str(numn))
else:
    print("\n" +str(num)+ "is not divisible by" +str(numn))