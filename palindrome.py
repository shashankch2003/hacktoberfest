def is_palindrome(value):
    # Convert the value to a string for uniform checking
    value = str(value)
    # Check if the string is the same when reversed
    return value == value[::-1]

# Test the function
user_input = input("Enter a string or number: ")
if is_palindrome(user_input):
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")
