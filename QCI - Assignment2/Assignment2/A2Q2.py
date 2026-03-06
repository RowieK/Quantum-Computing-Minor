def large_number(a, b, c):
    list_of_numbers = [a, b, c]
    largest_number = max(list_of_numbers)
    return list_of_numbers, largest_number

# Get inputs from user
# a = 12
# b = 5
# c = 8

# For input from user, uncomment the following lines:
a = int(input("Enter integer a: "))
b = int(input("Enter integer b: "))
c = int(input("Enter integer c: "))

# Output the result
list_of_numbers, largest_number = large_number(a, b, c)
print(list_of_numbers)
print(largest_number)