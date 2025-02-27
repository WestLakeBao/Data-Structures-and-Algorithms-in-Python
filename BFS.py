class Node(object):
    def __init__(self, name):
        self.name = name
        self.adjacencyList = []
        self.visited = False
        self.predecessor = None

class BFS(object):
    def bfs(self, startNode):
        queue = []
        queue.append(startNode)
        startNode.visited = True

        while queue:
            actualNode = queue.pop(0)
            print(actualNode.name)
            for n in actualNode.adjacencyList:
                if not n.visited:
                    n.visitied = True
                    queue.append(n)

if __name__ == '__main__':
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")

    node1.adjacencyList.append(node2)
    node1.adjacencyList.append(node3)
    node2.adjacencyList.append(node4)
    node4.adjacencyList.append(node5)

    bfs = BFS()
    bfs.bfs(node1) # A, B, C, D, E


