base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

result_operator = base ** exponent
print(f"{base} to the power of {exponent} is {result_operator}")


result_function = pow(base, exponent)
print(f"{base} to the power of {exponent} is {result_function}")
