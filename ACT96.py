def check_frequency(test_dict, target_value):
  
    return list(test_dict.values()).count(target_value)

my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 1}
val_to_check = 1

frequency = check_frequency(my_dict, val_to_check)
print(f"The frequency of {val_to_check} is: {frequency}")
