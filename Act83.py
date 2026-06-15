
my_set = {1, 2, 3}
print("Set of integers:", my_set)

my_set = {1.0, "Hello", (1, 2, 3)}
print("Mixed data type set:", my_set)

my_set = {1, 2, 3, 4, 3, 2}
print("Set after removing duplicates:", my_set)

my_set = set([1, 2, 3, 2])
print("Set from list:", my_set)
print()

num_set = set([0, 1, 3, 4, 5])
print("Original set:", num_set)

removed_element = num_set.pop()
print("Removed element:", removed_element)
print("Set after pop:", num_set)

print()