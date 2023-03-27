# Python programming, lab-2, Sasha Chekh
import math as m

print('Sasha Chekh')


def calculate_math_task(x, z):
    return x - (z / z - pow(x, 2) / 4) - pow(x, 2) / m.factorial(5)


def get_number(placeholder, allowed_type=int):
    input_val = input(f'{placeholder} ')
    if allowed_type(input_val):
        return allowed_type(input_val)
    raise Exception(f'Please input {allowed_type.__name__}')


x = get_number('Please input integer x: ')
z = get_number('Please input integer z: ')


print('y = ', calculate_math_task(int(x), int(z)))
