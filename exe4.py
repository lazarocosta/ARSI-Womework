import random

def G_Model(n, p, filename):
    file = open(filename + ".txt", "w")
    file.write("%d\n" % n)

    for x in range(0, n):
        for y in range(x + 1, n):
            random_number = random.random()
            if random_number < p:
                file.write("%d %d\n" % (x + 1, y + 1))


G_Model(2000, 0.0001, "random1")
G_Model(2000, 0.005, "random2")
