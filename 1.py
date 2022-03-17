# Python program for Dijkstra's single
# source shortest path algorithm. The program is
# for adjacency matrix representation of the graph
import csv
import random
class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist):

        dct = {x:y for x,y in zip(list(range(self.V)), [dist[i] for i in list(range(self.V))])}
        dct = {k: v for k, v in sorted(dct.items(), key=lambda item: item[1])}
        print(f"""Полученный путь: {'-'.join([str(i) for i in list(dct.keys())])}-{[str(i) for i in list(dct.keys())][0]}. Время в пути: {sum(list(dct.values()))}""")
        # print()
        # for x,y print():
        #     print(node, "\t\t", dist[node])

    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):

        # Initialize minimum distance for next node
        min = 1e7

        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):

        dist = [1e7] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)

            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                   sptSet[v] == False and
                   dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)
variant = int(input('Введите формат вводимых данных матрицы:\n1) ввод с клавитуры\n2)случайная генерация\n3)считывание из CSV  файла'))
try:
    vs = int(input("Введите количество вершин... "))

    matrix = []

    if variant == 1:

        for i in range(vs):
            st = input(f"Введите {i+1} строку матрицы через пробел... ")

            st = [int(i) for i in st.split()]

            if len(st) != vs:
                raise Exception
            else:
                matrix.append(st)
    elif variant == 2:
        for i in range(vs): matrix.append([random.randint(1,10) for i in range(vs)])

    elif variant == 3:
        with open('data.csv', encoding="utf-8-sig", mode="r") as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            for row in spamreader:
                matrix.append([int(i) for i in row])

    # Driver program
    g = Graph(vs)
    g.graph = matrix

    g.dijkstra(3)
except Exception as e:
    print(e)
