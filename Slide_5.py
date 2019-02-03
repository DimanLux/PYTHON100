def math_1(x, y, z, f):
    res = (((x * (y - x)) / z) + x + ((f + z) / (f ** y)) - ((z - f) / z)) / (((z + f) / z ** y) - f)
    return res


if __name__ == "__main__":
    print("output1 = " + str(math_1(5, 2.3, 2, 7.8)))
    print("output2 = " + str(math_1(1234, 37872, 1231, 12314)))
