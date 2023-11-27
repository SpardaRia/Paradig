""" Задача №2
Написать точно такую же процедуру, но в декларативном стиле """


def sort_list_declarative(numbers):
    numbers.sort(reverse=True)
    return numbers

print(f"Declarative: {sort_list_declarative([45, -2, 0, 566, 58, -658, 15, 0])}")