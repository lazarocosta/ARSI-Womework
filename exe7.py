import random


def full_connected(file, m0, my_array):
    for x in range(1, m0 + 1):
        for z in range(x + 1, m0 + 1):
            my_array.append(x)
            my_array.append(z)
            file.write("%d %d\n" % (x, z))


def BA_Model(n, m0, m, filename):
    my_array = []
    file = open(filename + ".txt", "w")
    file.write("%d\n" % n)
    full_connected(file, m0, my_array)
    for x in range(m0 + 1, n + 1):
        edges_added = []
        n_number_selected = 0
        while n_number_selected < m:
            random_value = random.randint(0, len(my_array) - 1)
            random_node_selected = my_array[random_value]
            if random_node_selected not in edges_added:
                edges_added.append(random_node_selected)
                my_array.append(random_node_selected)
                file.write("%d %d\n" % (x, random_node_selected))
            else:
                n_number_selected -= 1
            n_number_selected += 1
        for nodes_selected in range(0, m):
            my_array.append(x)
    file.close()


BA_Model(2000, 3, 1, "ba1")
BA_Model(2000, 5, 2, "ba2")
