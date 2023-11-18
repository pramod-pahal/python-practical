# Create a tuple
my_tuple = (1, 2, 3, 4, 2, 5, 6, 2)

# (i) Delete: Tuples are immutable, so you can't delete individual elements, but you can delete the entire tuple.
del my_tuple
# Uncommenting the following line would result in an error:
# print(my_tuple)

# Recreate the tuple for the next methods
my_tuple = (1, 2, 3, 4, 2, 5, 6, 2)

# (ii) Count: Count occurrences of a specific element
element_to_count = 2
count = my_tuple.count(element_to_count)
print(f"Count of {element_to_count}: {count}")

# (iii) Index: Find the index of the first occurrence of a specific element
element_to_find = 5
index = my_tuple.index(element_to_find)
print(f"Index of {element_to_find}: {index}")
