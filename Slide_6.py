def task_1(n):
    m = len(n) % 5
    list_1 = [i + 1 for i in range((m + 2) * 2)]
    return list_1


def task_2(n):
    m = len(n) % 5
    list_1 = [i + 1 for i in range((m + 2) * 2)]
    list_double = list_1 + [i+1 for i in list_1]
    return list_double


def task_3(n):
    m = len(n) % 5
    list_1 = [i + 1 for i in range((m + 2) * 2)]
    list_double = list_1 + [i+1 for i in list_1]
    list_descend = list_double[1: -1]
    return list_descend


def task_4(n):
    m = len(n) % 5
    list_1 = [i + 1 for i in range((m + 2) * 2)]
    list_double = list_1 + [i + 1 for i in list_1]
    list_index = [list_double[i] for i in range(1, len(list_double), 3)]
    return list_index


def task_5(n):
    m = len(n) % 5
    list_1 = [i + 1 for i in range((m + 2) * 2)]
    list_double = list_1 + [i + 1 for i in list_1]
    list_second_third = [list_double[i] for i in range(round(len(list_double) / 3), round(2 * len(list_double) / 3))]
    return list_second_third


if __name__ == "__main__":
    print(task_1("дмитрийяковлев"))
    print(task_2("дмитрийяковлев"))
    print(task_3("дмитрийяковлев"))
    print(task_4("дмитрийяковлев"))
    print(task_5("дмитрийяковлев"))
