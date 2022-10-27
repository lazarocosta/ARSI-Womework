import matplotlib.pyplot as plt
import numpy as np
import powerlaw
import collections


def exe8(filename):
    file = open(filename + ".txt", "r")
    number_nodes_string = file.readline()
    number_nodes = int(number_nodes_string.split("\n")[0])

    myList = []
    for line in file:
        numbers = line.split()
        myList.append(numbers[0])
        myList.append(numbers[1])

    frequency = collections.Counter(myList)
    sorted_keys = sorted(frequency.keys())
    degree_0 = np.array([])
    for key in sorted_keys:
        degree_0 = np.append(degree_0, frequency[key])

    degree_0 = degree_0.astype(int)
    degree = np.bincount(degree_0)
    degree = np.delete(degree, 0)

    XareAtLeatX = number_nodes
    data = np.array([])
    for key in degree:

        XareAtLeatX -= key  # x
        if XareAtLeatX == 0:
            break
        data = np.append(data, XareAtLeatX)

    dict_aux = dict.fromkeys(data)
    data = list(dict_aux)

    fig = plt.figure()
    fit = powerlaw.Fit(np.array(data) + 0)
    fit.power_law.plot_ccdf(linestyle='--', color='r')
    fit.plot_ccdf()

    print(filename +".txt")
    print(f'alpha={fit.power_law.alpha + 1} sigma={fit.power_law.sigma}')
    fit_number = "alpha=" + str(np.around(fit.power_law.alpha + 1, 2))
    plt.xlabel('Degree')
    plt.ylabel('frequency sample >x')
    plt.legend([fit_number, "data"])
    plt.title(filename)
    plt.savefig("power_law_" + filename + ".png")
    plt.show()

    #print(fit.power_law.xmin)
    #print(fit.power_law.D)


exe8("ba1")
print("\n")
exe8("ba2")
