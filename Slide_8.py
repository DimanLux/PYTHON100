def task_1(km):
    r = 0
    d = 0
    while r < km:
        d += 1
        r += (2 ** d)
    return str(d) + " дней"


def task_2(km):
    r = 0
    d = 0
    lst_of_km = []
    for i in range(2, km):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst_of_km.append(i)
    while r < km:
        r += lst_of_km[d]
        d += 1
    return d


def task_3(days):
    r = 10
    total = 0
    d = 0
    while d < days:
        if d % 2 == 1:
            r *= 1.15
        d += 1
        total += r
    return str(round(total)) + ' km'


def task_4a(totrun):
    r = 10
    d = 0
    while r < totrun:
        r *= 1.1
        d += 1
    return str(d) + " дней"


def task_4b(total):
    r = 10
    d = 0
    while r < total:
        r *= 1.1
        d += 1
    if d % 2 == 0:
        return str(d) + " дня"
    else:
        return str(d) + " дней"


if __name__ == "__main__":
    print(task_1(1000))
    print(task_2(1000))
    print(task_3(30))
    print(task_4a(20))
    print(task_4b(100))
