def is_between(a, b, c):
    if a < c < b:
        return True
    else:
        return False

# Get inputs from user
a = int(input("Enter integer a: "))
b = int(input("Enter integer b: "))
c = int(input("Enter integer c: "))

# Output the result
print(is_between(a, b, c))