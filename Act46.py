while True:
    num = int(input("Enter a decimal number (0 to exit): "))
    
    if num == 0:
        print("Exiting...")
        break
    
    binary = ""
    temp = num
    
    while temp > 0:  # inner loop
        remainder = temp % 2
        binary = str(remainder) + binary
        temp = temp // 2
    
    print("Binary of", num, "is:", binary)