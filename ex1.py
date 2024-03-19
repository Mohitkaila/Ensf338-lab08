class GraphNode:
    def __init__(self, data):
        self.data = data

class Graph:
    def __init__(self):
        self.adjacency_list = {}  # Dictionary: key = node, value = list of (neighbor, weight) tuples

    def addNode(self, data):
        node = GraphNode(data)
        if data not in self.adjacency_list:
            self.adjacency_list[data] = []
        return node

    def removeNode(self, node):
        if node.data in self.adjacency_list:
            # Remove the node from adjacency list
            del self.adjacency_list[node.data]
            # Remove edges to this node
            for neighbors in self.adjacency_list.values():
                for neighbor, _ in neighbors.copy():
                    if neighbor == node.data:
                        neighbors.remove((neighbor, 1))

    def addEdge(self, n1, n2, weight=1):
        if n1 not in self.adjacency_list:
            self.addNode(n1)
        if n2 not in self.adjacency_list:
            self.addNode(n2)
        self.adjacency_list[n1].append((n2, weight))
        self.adjacency_list[n2].append((n1, weight))  # Since the graph is undirected

    def removeEdge(self, n1, n2):
        self.adjacency_list[n1] = [neighbor for neighbor in self.adjacency_list[n1] if neighbor[0] != n2]
        self.adjacency_list[n2] = [neighbor for neighbor in self.adjacency_list[n2] if neighbor[0] != n1]

    def importFromFile(self, file):
        try:
            with open(file, 'r') as f:
                lines = f.readlines()
            if not lines[0].strip().startswith("strict graph"):
                return None
            self.adjacency_list = {}
            for line in lines[1:]:
                if '--' in line:
                    parts = line.split('--')
                    node1 = parts[0].strip()
                    rest = parts[1].split('[')
                    node2 = rest[0].strip()
                    weight = 1
                    if len(rest) > 1:
                        weight_attr = rest[1].split('=')[1].rstrip('];\n')
                        weight = int(weight_attr)
                    self.addEdge(node1, node2, weight)
        except Exception as e:
            print(f"Error importing from file: {e}")
            return None

# Example usage
graph = Graph()
graph.importFromFile('your_graph_file.dot')  # Replace 'your_graph_file.dot' with your GraphViz file path
