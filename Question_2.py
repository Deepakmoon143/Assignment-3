def reverse_string(input_string):
    reversed_str = ""
    for i in input_string:
        reversed_str = i + reversed_str
    return reversed_str

user_input = input("Enter a string: ")

reversed_result = reverse_string(user_input)
print(f"Original String:{user_input}")
print(f"Reversed String:{reversed_result}")
