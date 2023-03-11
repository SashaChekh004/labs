from comment_parser import comment_parser


# # Python programming, lab-2, Sasha Chekh
#
# comments = comment_parser.extract_comments('lab-2.py', mime='text/x-c')
#
# print(comments)

# def calculateMathTask(x,y,z)

def calculate_math_task(x, y, z):
    return ((15 - x / y) / pow(33, y) + 19.3) + z


x, y, z = input('input x, y, z: ').split()

print(calculate_math_task(int(x), int(y), int(z)))
