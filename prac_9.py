numbers = [int(input("Enter number {}: ".format(i+1))) for i in range(3)]
numbers.sort()
lowest, second_largest, largest = numbers[0], numbers[1], numbers[2]
print("Lowest:", lowest)
print("Second Largest:", second_largest)
print("Largest:", largest)
