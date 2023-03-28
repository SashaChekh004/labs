# Python programming, lab-2, Sasha Chekh
print('Sasha Chekh')


def calculate_math_task(x, y, z):
    return ((15 - x / y) / pow(33, y) + 19.3) + z


def get_number(var_name, allowed_type=int):
    input_val = input(f'Please put variable {var_name} for calculation: ')
    try:
        converted_value = allowed_type(input_val)
        return converted_value
    except ValueError:
        print(f'Please input {allowed_type.__name__}')


x = get_number('x')
y = get_number('y')
z = get_number('z')

print(calculate_math_task(x, y, z))
