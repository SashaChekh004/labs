def write_lines(task_text):
    task_name, assignee_name, mentor_name = task_text.split(',')

    repeated_teacher_name = ','.join([mentor_name for _ in range(45)])
    print(task_name)
    print(assignee_name)
    print(repeated_teacher_name)


write_lines('Introduction to programming: Task 1, Sasha Chekh, Andriy')

print((15 - 13.1 / 3)/(pow(33, 2) + 19.3) + 3.3)
