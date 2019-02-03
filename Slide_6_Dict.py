def task_1(n):
    m = len(n) % 5
    list_1 = {i + 1: i + 1 for i in range((m + 2) * 2)}
    return list_1


def task_2(n):
    m = (len(n) % 5 + 2) * 2
    list_1 = {i + 1: i + 1 for i in range(m)}
    for i in range(m):
      list_1[(m+i)+1] = i + 2
    list_double = list_1
    return list_double


# def task_3(n):
#     m = (len(n) % 5 + 2) * 2
#     list_1 = {i + 1 : i + 1 for i in range(m)}
#     for i in range(m):
#       list_1[(m+i)+1] = i + 2
#     list_double = list_1
#     list_descend = {i: list_double[i]}
# # for i in range(1, len(d)-1)
#     return list_descend

if __name__ == "__main__":
    print(task_1("дмитрийяковлев"))
    print(task_2("дмитрийяковлев"))
    # print(task_3("дмитрийяковлев"))