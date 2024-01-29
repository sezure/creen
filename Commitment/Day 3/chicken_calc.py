for x in range(0, 21):
    for y in range(0, 34):
        z = 100 - x - y
        if 5 * x + 3 * y + z / 3 == 100:
            print("公鸡数量：", x, "母鸡数量：", y, "小鸡数量：", z)