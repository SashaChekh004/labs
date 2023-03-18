# Python programming, lab-2, Sasha Chekh
import math

print('Sasha Chekh')

def calculate_math_task(x, z):
    return x - (z / z - pow(x, 2) / 4) - pow(x, 2) / math.factorial(5)

x, z = input('Please put variables x, z for calculation: ').split()

print("y = ", calculate_math_task(int(x), int(z)))
