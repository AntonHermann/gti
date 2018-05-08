for i in range(12):
    # print("{0} {1:03d}: {1:08b}".format("->" if (i % 3 == 0) else "  ", i))
    print("{0} {1:03d}: {1:b}".format("->" if (i % 3 == 0) else "  ", i))