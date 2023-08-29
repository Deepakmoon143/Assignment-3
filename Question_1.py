def sum_list_numbers(num):
    return sum(num)

user_input = input("Enter a list of numbers separated by spaces: ")
list = [int(i) for i in user_input.split()]


result = sum_list_numbers(list)

print(f"Sum of the numbers:{result}")




