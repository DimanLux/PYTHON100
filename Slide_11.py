def task_2(numb):
    return len(str(abs(numb)))


def task_3(string):
    if string == string[::-1]:
        return True
    else:
        return False


if __name__ == "__main__":
    print(task_2(-609))
    print(task_3('aabbaac'))


