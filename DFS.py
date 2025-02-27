class Node(object):
    def __init__(self, name):
        self.name = name
        self.adjacencyList = []
        self.visited = False
        self.predecessor = None


class DFS(object):
    def dfs(self, node):
        node.visited = True
        print(node.name)

        for n in node.adjacencyList:
            if not n.visited:
                self.dfs(n)

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

    dfs = DFS()
    dfs.dfs(node1) # A, B, D, E, C

