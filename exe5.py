import datetime


def read_file(file, all_nodes, nodes):
    # read file
    for x in file:
        numbers = x.split()

        node0 = numbers[0]
        node1 = numbers[1]

        if node0 not in all_nodes:
            all_nodes[node0] = node0

        if node1 not in all_nodes:
            all_nodes[node1] = node1

        # adiciono as arestas nas duas direçoes
        if node0 in nodes:
            nodes[node0].append(node1)
        else:
            nodes[node0] = [node1]

        # adiciono as arestas nas duas direçoes
        if node1 in nodes:
            nodes[node1].append(node0)
        else:
            nodes[node1] = [node0]


def size_gigant_component(filename):
    filename = filename + ".txt"
    file = open(filename, "r")
    number_nodes = file.readline()
    nodes = {}
    nodes_visited = []

    all_nodes = {}  # guarda todos os nós que têm arestas

    nodes_to_visit = []
    g_c_size = 0
    today = datetime.datetime.now()
    read_file(file, all_nodes, nodes)

    while len(all_nodes) > 0:
        g_c_size_local = 1
        actual_node = next(iter(all_nodes))
        all_nodes.pop(actual_node, None)

        nodes_visited.append(actual_node)

        nodes_to_visit.append(actual_node)
        while len(nodes_to_visit) > 0:
            this_node = nodes_to_visit.pop(0)
            if this_node in all_nodes:
                all_nodes.pop(this_node, None)
                g_c_size_local += 1
            if this_node in nodes:
                for edge_of_node_visited in nodes[this_node]:
                    if edge_of_node_visited not in nodes_visited:
                        if edge_of_node_visited in all_nodes:
                            all_nodes.pop(edge_of_node_visited, None)
                            g_c_size_local += 1
                        nodes_to_visit.append(edge_of_node_visited)
                        nodes_visited.append(edge_of_node_visited)
        if g_c_size_local > g_c_size:
            g_c_size = g_c_size_local

    today2 = datetime.datetime.now()
    time_diff = today2 - today
    # print(f"Time {time_diff}")
    return g_c_size


print("exercicio 5")
g_c_size = size_gigant_component("random1")
print("random1")
print("size: " + str(g_c_size))
print("\n")
g_c_size = size_gigant_component("random2")
print("random2")
print("size: " + str(g_c_size))
