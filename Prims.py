import heapq

class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.predecessor = None
        self.adjacencyList = []

    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, weight, start, target):
        self.weight = weight
        self.start = start
        self.target = target

    # defining comparators less_than and equals
    def __lt__(self, other):
        return self.weight < other.weight

    def __eq__(self, other):
        if not other:
            return False
        if not isinstance(other, Edge):
            return False
        return self.weight == other.weight

class prims(object):
    def __init__(self, unvisitedList):
        self.unvisitedList = unvisitedList
        self.spanningTree = []
        self.edgeHeap = []
        self.fullCost = 0

    def calculateSpanningTree(self, vertex):
        self.unvisitedList.remove(vertex)
        while self.unvisitedList:
            for edge in vertex.adjacencyList:
                if edge.target in self.unvisitedList:
                    heapq.heappush(self.edgeHeap, edge)
            minEdge = heapq.heappop(self.edgeHeap)
            self.spanningTree.append(minEdge)
            print("Edge added to the spanning tree", minEdge.start.name, minEdge.target.name)
            self.fullCost += minEdge.weight
            vertex = minEdge.target
            self.unvisitedList.remove(vertex)

    def getSpanningTree(self):
        return self.spanningTree

if __name__ == '__main__':
    vertex1 = Vertex("A")
    vertex2 = Vertex("B")
    vertex3 = Vertex("C")

    edge1 = Edge(100, vertex1, vertex2)
    edge2 = Edge(100, vertex2, vertex1)
    edge3 = Edge(1000, vertex1, vertex3)
    edge4 = Edge(1000, vertex3, vertex1)
    edge5 = Edge(0.01, vertex3, vertex2)
    edge6 = Edge(0.01, vertex2, vertex3)

    vertex1.adjacencyList.append(edge1)
    vertex1.adjacencyList.append(edge3)
    vertex2.adjacencyList.append(edge2)
    vertex2.adjacencyList.append(edge6)
    vertex3.adjacencyList.append(edge4)
    vertex3.adjacencyList.append(edge5)

    unvisitedList = []
    unvisitedList.append(vertex1)
    unvisitedList.append(vertex2)
    unvisitedList.append(vertex3)

    algo = prims(unvisitedList)
    algo.calculateSpanningTree(vertex1)
    # Edge added to the spanning tree A B
    # Edge added to the spanning tree B C

