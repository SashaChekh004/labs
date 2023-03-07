def writelines(line1Text, line2Text, line3Text):
    print(line1Text)
    print(line2Text)

    repeatedTeacherName = ''

    for i in range(45):
        if i == 44:
            repeatedTeacherName += line3Text
        else:
            repeatedTeacherName += f'{line3Text}, '
    print(repeatedTeacherName)


writelines("Introduction to programming: Task 1", "Sasha Chekh", "Andriy")


print( ( 15 - 13.1 / 3 ) / (pow(33, 2) + 19.3) + 3.3)