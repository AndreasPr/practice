class Graph:
    def __init__ (self, V):
        self.V = V
        self.adj = [[] for i in range(self.V)]
    
    def NumberOfConnectedComponents(self):
        visited = [False for i in range(self.V)]

        count = 0
        
        for v in range(self.V):
            if visited[v] == False:
                self.DFSUtil(v, visited)
                count+=1
        return count

    def DFSUtil(self, v, visited):
        visited[v] = True

        for i in self.adj[v]:
            if not visited[i]:
                self.DFSUtil(i, visited)

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)


if __name__ == "__main__":

    vertices = int(input())
    numberOfEdges = int(input())
    g = Graph(vertices)
    for _ in range(numberOfEdges):
        a, b = input().split()
        g.addEdge(int(a), int(b))
    
    print(g.NumberOfConnectedComponents())
