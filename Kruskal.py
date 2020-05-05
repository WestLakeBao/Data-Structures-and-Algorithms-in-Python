class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.node = None

class Node(object):
    def __init__(self, height, nodeId, parent):
        self.height = height
        self.nodeId = nodeId
        self.parent = parent

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

class DisjointSet(object):
    def __init__(self, vertexList):
        self.vertexList = vertexList
        self.rootNodes = []
        self.nodeCount = 0
        self.setCount = 0
        self.makeSets(vertexList)

    def find(self, node):
        current = node
        while current.parent:
            current = current.parent

        root = current
        current = node

        while current != root:
            temp = current.parent
            current.parent = root
            current = temp

        return root.nodeId

    def merge(self, node1, node2):
        index1 = self.find(node1)
        index2 = self.find(node2)

        if index1 == index2:
            return

        root1 = self.rootNodes[index1]
        root2 = self.rootNodes[index2]

        if root1.height < root2.height:
            root1.parent = root2
        elif root1.height > root2.height:
            root2.parent = root1
        else:
            root2.parent = root1
            root1.height += 1

    def makeSets(self, vertexList):
        for v in vertexList:
            self.makeSet(v)

    def makeSet(self, vertex):
        node = Node(0, len(self.rootNodes), None)
        vertex.node = node
        self.rootNodes.append(node)
        self.setCount += 1
        self.nodeCount += 1

class KruskalAlgorithm(object):
    def spanningTree(self, vertexList, edgeList):
        disjointSet = DisjointSet(vertexList)
        spanningTree = []
        edgeList.sort()
        for edge in edgeList:
            u = edge.start
            v = edge.target
            if disjointSet.find(u.node) != disjointSet.find(v.node):
                spanningTree.append(edge)
                disjointSet.merge(u.node, v.node)
        for edge in spanningTree:
            print(edge.start.name, "-", edge.target.name)

if __name__ == '__main__':
    vertexA = Vertex("A")
    vertexB = Vertex("B")
    vertexC = Vertex("C")
    vertexD = Vertex("D")
    vertexE = Vertex("E")
    vertexF = Vertex("F")
    vertexG = Vertex("G")

    edgeAB = Edge(2, vertexA, vertexB)
    edgeAC = Edge(6, vertexA, vertexC)
    edgeAE = Edge(5, vertexA, vertexE)
    edgeAF = Edge(10, vertexA, vertexF)
    edgeBD = Edge(3, vertexB, vertexD)
    edgeBE = Edge(3, vertexB, vertexE)
    edgeCD = Edge(1, vertexC, vertexD)
    edgeCF = Edge(2, vertexC, vertexF)
    edgeDE = Edge(4, vertexD, vertexE)
    edgeDG = Edge(5, vertexD, vertexG)
    edgeFG = Edge(5, vertexF, vertexG)

    vertexList = []
    vertexList.append(vertexA)
    vertexList.append(vertexB)
    vertexList.append(vertexC)
    vertexList.append(vertexD)
    vertexList.append(vertexE)
    vertexList.append(vertexF)
    vertexList.append(vertexG)

    edgeList = []
    edgeList.append(edgeAB)
    edgeList.append(edgeAC)
    edgeList.append(edgeAE)
    edgeList.append(edgeAF)
    edgeList.append(edgeBD)
    edgeList.append(edgeBE)
    edgeList.append(edgeCD)
    edgeList.append(edgeCF)
    edgeList.append(edgeDE)
    edgeList.append(edgeDG)
    edgeList.append(edgeFG)

    algo = KruskalAlgorithm()
    algo.spanningTree(vertexList, edgeList)
    # C - D
    # A - B
    # C - F
    # B - D
    # B - E
    # D - G