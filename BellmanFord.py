import sys

class Edge(object):
    def __init__(self, weight, start, target):
        self.weight = weight
        self.start = start
        self.target = target

class Node(object):
    def __init__(self, name):
        self.name = name
        self.predecessor = None
        self.adjacencyList = []
        self.minDistance = sys.maxsize #infinity

class BellmanFord(object):
    HAS_CYCLE = False

    def calculateShortestPath(self, vertexList, edgeList, start):
        start.minDistance = 0

        for i in range(len(vertexList) - 1):
            for edge in edgeList:
                u = edge.start
                v = edge.target

                newDistance = u.minDistance + edge.weight

                if newDistance < v.minDistance:
                    v.minDistance = newDistance
                    v.predecessor = u

        for edge in edgeList:
            if self.hasCycle(edge):
                print("Negative cycle detected...")
                self.HAS_CYCLE = True
                return

    def hasCycle(self, edge):
        if edge.start.minDistance + edge.weight < edge.target.minDistance:
            return True
        return False

    def getShortestPath(self, target):
        if not self.HAS_CYCLE:
            print("Shortest path exists with value ", target.minDistance)
            while target:
                print(target.name)
                target = target.predecessor
        else:
            print("Negative cycles detected")

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

    vertexList = (nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeG, nodeH)
    edgeList = (edgeAB, edgeAH, edgeAE, edgeBD, edgeBC, edgeBH, edgeHC, edgeHF, edgeEH, edgeEF, edgeEG, edgeFC, edgeFG, edgeCD, edgeCG, edgeDG)

    algo = BellmanFord()
    algo.calculateShortestPath(vertexList, edgeList, nodeA)
    algo.getShortestPath(nodeG)

    # Shortest path exists with value  25
    # G
    # C
    # F
    # E
    # A