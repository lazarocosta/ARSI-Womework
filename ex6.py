import shutil
from exe4 import G_Model
import matplotlib.pyplot as plt
import os
from exe5 import size_gigant_component

folder = 'folder-exe6'
path = os.getcwd() + "/" + folder
if not os.path.isdir(path):
    os.makedirs(path)

# delete the content of the "folder-exe6" folder
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))


def generateGrph(n, lowestPValue, HighestPValue, step, folder):
    currentPValue = lowestPValue

    while currentPValue <= HighestPValue:
        G_Model(n, currentPValue, "./" + folder + "/" + str(currentPValue))
        currentPValue += step
        currentPValue = round(currentPValue, 4)


def calculate_size_gigant_component_inside_folder(folder):
    x = []
    y = []
    for filename in os.listdir(folder):
        filename_without_extention = filename.split(".txt")[0]
        s_g_component = size_gigant_component("./" + folder + "/" + filename_without_extention)
        y.append(s_g_component)
        x.append(float(filename_without_extention))

    plt.plot(x, y)

    plt.xlabel('P')
    plt.ylabel('size_gigant_component')
    plt.savefig("exe6_plot.png")
    plt.show()


generateGrph(2000, 0.0001, 0.005, 0.0001, "folder-exe6")
calculate_size_gigant_component_inside_folder(folder)
