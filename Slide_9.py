def task_1(n):
    l = [1, 1]
    while len(l) <= n:
        l.append(l[-1] + l[-2])
    return l


def task_2(n):
    l = [1, 1, 1]
    while len(l) <= n:
        l.append(l[-1] + l[-2] + l[-3])
    return l


def task_3(n):
    a = [i**2 for i in range(1, n, 2)]
    return a


def task_4(h, w):
    for i in range(h+1):
        if i == 0 or i == h:
            print("*" * w)
        else:
            print("*" + " " * (w-2) + "*")


def task_5(a, b):
    summ = 0
    mult = 1
    for i in range(a, b+1):
        summ += i
        mult *= i
    return summ, mult


def task_6(a, b):
    chetn = []
    nechetn = []
    for i in range(a, b):
            if i % 2 == 0:
                chetn.append(i)
            else:
                nechetn.append(i)
    return nechetn, chetn


def task_7(inp_list):
    return [i for i in inp_list if i >= 0], [i for i in inp_list if i < 0]


if __name__ == "__main__":
    print(task_1(8))
    print(task_2(8))
    print(task_3(50))
    print(task_4(6, 6))
    print(task_5(1, 5))
    print(task_6(1, 10))
    print(task_7([1, 4, -10, 0, -876, -87]))