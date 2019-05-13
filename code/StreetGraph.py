class Node(object):
    def __init__(self,Id,lat,lon,h,risk):
        ''' h in meters
        '''
        self.Id = str(Id)
        self.lat = lat
        self.lon = lon
        self.h = h
        self.risk = risk
    def setRisk(self,risk):
        self.risk = risk
    def getId(self):
        return self.Id
    def __str__(self):
        return self.Id

class Edge(object):
    def __init__(self, src, dest):
        self.src = src
        self.dest = dest
    def setWeight(self,risk,comf):
        self.weight = [comf,risk]
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def getWeight(self):
        ''' edge weight given by [comfort,risk] '''
        return self.weight
    def __str__(self):
        return str(self.src) + '->' + str(self.dest)

class Graph(object):
    def __init__(self):
        self.nodes = []
        self.edges = {}
    def addNode(self, node):
        if node in self.nodes:
            raise ValueError('Duplicate node')
        else:
            self.nodes.append(node)
            self.edges[node] = [[],[]]
    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not(src in self.nodes and dest in self.nodes):
            raise ValueError('Node not in graph')
        if dest not in self.edges[src]:
            self.edges[src][0].append(dest)
            self.edges[src][1].append(edge.getWeight())
    def childrenOf(self, node):
        return self.edges[node][0]
    def hasNode(self, node):
        return node in self.nodes
    def __str__(self):
        res = '{\n'
        for k in self.edges:
            K = k.getId()
            res = res + str(K) + ':\n'
            for el in range(len(self.edges[k][0])):
                d = self.edges[k][0][el]
                D = d.getId()
                res = res + '\t' + str(D) + '\t' + str(self.edges[k][1][el]) + '\n'
        return res + '}'