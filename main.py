def is_even(number):
    return number % 2 == 0

number_check = 10
result = is_even(number_check)

if result:
    print(f"{number_check} є парним числом.")
else:
    print(f"{number_check} є непарним числом.")
