# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


print(is_even(3))

# Read a number from the keyboard


# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

while not 0:
    num = input("Enter a number: ")
    num = int(num)
    if num % 2 == 0:
        print("Even!")
        continue
    else:
        print("Odd")
        continue
