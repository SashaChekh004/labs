# Python programming, lab-2, Sasha Chekh
print('Sasha Chekh')
def calculate_math_task(x, y, z):
    return ((15 - x / y) / pow(33, y) + 19.3) + z

x, y, z = input('Please put variables x, y, z for calculation: ').split()

print(calculate_math_task(int(x), int(y), int(z)))
