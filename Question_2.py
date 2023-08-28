def reverse_string(input_string):
    reversed = ""
    for i in input_string:
        reversed = i + reversed
    return reversed

user_input = input("Enter a string: ")

reversed_result = reverse_string(user_input)
print(f"Original String:{user_input}")
print(f"Reversed String:{reversed_result}")
