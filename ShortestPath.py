import sys
import heapq

class Edge(object):
    def __init__(self, weight, start, target):
        self.weight = weight
        self.start = start
        self.target = target


class Node(object):
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.adjacencyList = []
        self.minDistance = sys.maxsize #infinity

    # defining comparators less_than and equals
    def __lt__(self, other):
        return self.minDistance < other.minDistance

    def __eq__(self, other):
        if not other:
            return False
        if(not isinstance(other, Node)):
            return False
        return self.minDistance == other.minDistance


class Algorithm(object):
    def calculateShortestPath(self, start):
        q = []
        start.minDistance = 0
        heapq.heappush(q, start)

        while q:
            actual = heapq.heappop(q)
            for edge in actual.adjacencyList:
                u = edge.start
                v = edge.target
                newDistance = u.minDistance + edge.weight

                if newDistance < v.minDistance:
                    v.minDistance = newDistance
                    v.predecessor = u
                    heapq.heappush(q, v)

    def getShortestPath(self, target):
        print("The shortest path to vertex is ", target.minDistance)

        node = target

        while node:
            print(node.name)
            node = node.predecessor



if __name__ == '__main__':
    nodeA = Node("A")
    nodeB = Node("B")
    nodeC = Node("C")
    nodeD = Node("D")
    nodeE = Node("E")
    nodeF = Node("F")
    nodeG = Node("G")
    nodeH = Node("H")

    edgeAB = Edge(5, nodeA, nodeB)
    edgeAH = Edge(8, nodeA, nodeH)
    edgeAE = Edge(9, nodeA, nodeE)
    edgeBD = Edge(15, nodeB, nodeD)
    edgeBC = Edge(12, nodeB, nodeC)
    edgeBH = Edge(4, nodeB, nodeH)
    edgeHC = Edge(7, nodeH, nodeC)
    edgeHF = Edge(6, nodeH, nodeF)
    edgeEH = Edge(5, nodeE, nodeH)
    edgeEF = Edge(4, nodeE, nodeF)
    edgeEG = Edge(20, nodeE, nodeG)
    edgeFC = Edge(1, nodeF, nodeC)
    edgeFG = Edge(13, nodeF, nodeG)
    edgeCD = Edge(3, nodeC, nodeD)
    edgeCG = Edge(11, nodeC, nodeG)
    edgeDG = Edge(9, nodeD, nodeG)

    nodeA.adjacencyList.append(edgeAB)
    nodeA.adjacencyList.append(edgeAH)
    nodeA.adjacencyList.append(edgeAE)
    nodeB.adjacencyList.append(edgeBD)
    nodeB.adjacencyList.append(edgeBC)
    nodeB.adjacencyList.append(edgeBH)
    nodeH.adjacencyList.append(edgeHC)
    nodeH.adjacencyList.append(edgeHF)
    nodeE.adjacencyList.append(edgeEH)
    nodeE.adjacencyList.append(edgeEF)
    nodeE.adjacencyList.append(edgeEG)
    nodeF.adjacencyList.append(edgeFC)
    nodeF.adjacencyList.append(edgeFG)
    nodeC.adjacencyList.append(edgeCD)
    nodeC.adjacencyList.append(edgeCG)
    nodeD.adjacencyList.append(edgeDG)

    list = (nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeG, nodeH)

    algo = Algorithm()
    algo.calculateShortestPath(nodeA)
    algo.getShortestPath(nodeG)
