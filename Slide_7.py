def task_1(a, b):
    out = ""
    for _ in range(a):
        out += b + '\n'
    return out


def task_2(z):
    out = ""
    for i in range(z):
        out += ((i + 1) * '=') + '\n'
    return out


def task_3(a):
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d


def task_4(a):
    d = {}
    for word in a.split():
        key = "слов длинной " + str(len(word))
        if key in d:
            d[key] += 1
        else:
            d[key] = 1
    return d


if __name__ == "__main__":
    print(task_1(5, "tre"))
    print(task_2(6))
    print(task_3("aaaaaabbbccdhhhhhhhabra"))
    print(task_4('ab bbc cd oioioioi f fff'))

