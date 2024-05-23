from Queue import Queue

class Empty(Exception):
    pass

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connections = {}
        self.color = 'white'
        self.dist = 0
        self.pred = None

    def __str__(self):
        result = f'({self.id})\n'
        for key in self.connections.keys():
            result += f'--{self.connections[key]}-> ({key})\n'
        return result[:len(result)-1]

    def getEdges(self):
        result = []
        for key in self.connections.keys():
            result.append((self.id, key, self.connections[key]))
        return result

    def addConnectionTo(self, nbr, weight=0):
        self.connections[nbr] = weight

    def getConnectionsTo(self):
        return self.connections.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connections[nbr]

    def setColor(self, color):
        self.color = color

    def setDistance(self, dist):
        self.dist = dist

    def setPredecesor(self, pred):
        self.pred = pred

    def getColor(self):
        return self.color

    def getDistance(self):
        return self.dist

    def getPredecesor(self):
        return self.pred

class Graph:
    def __init__(self):
        self.verts = {}
        self._n = 0

    def __contains__(self, key):
        return key in self.verts.keys()

    def addVertex(self, key):
        self._n += 1
        newVert = Vertex(key)
        self.verts[key] = newVert

    def addEdge(self, fromVertKey, toVertKey, weight=0):
        if fromVertKey not in self.verts.keys():
            self.addVertex(fromVertKey)
        if toVertKey not in self.verts.keys():
            self.addVertex(toVertKey)
        self.verts[fromVertKey].addConnectionTo(toVertKey, weight)

    def addEdgeUd(self, vertKey1, vertKey2, weight=0):
        if vertKey1 not in self.verts.keys():
            self.addVertex(vertKey1)
        if vertKey2 not in self.verts.keys():
            self.addVertex(vertKey2)
        self.verts[vertKey1].addConnectionTo(vertKey2, weight)
        self.verts[vertKey2].addConnectionTo(vertKey1, weight)

    def getVertex(self, vertKey):
        if vertKey in self.verts.keys():
            return self.verts[vertKey]
        else:
            return None

    def getVertices(self):
        return self.verts.keys()

    def getEdges(self):
        result = []
        for key in self.verts.keys():
            vert = self.verts[key]
            result.extend(vert.getEdges())
        return result

    def dotRepr(self):
        result = "digraph finite_state_machine {\nnode [shape = circle];\n"
        for edge in self.getEdges():
            result += f"""{edge[0]} -> {edge[1]} [ label = "{edge[2]}" ];\n"""
        return result + '}'

    def breadthFirstSearch(self, startKey):
        for key in self.verts.keys():
            self.verts[key].setColor('white')
        startVert = self.verts[startKey]
        startVert.setDistance(0)
        startVert.setPredecesor(None)
        procQueue = Queue()
        procQueue.enqueue(startVert)
        while len(procQueue) > 0:
            currentVert = procQueue.dequeue()
            for nbrKey in currentVert.getConnectionsTo():
                nbr = self.verts[nbrKey]
                if (nbr.getColor() == 'white'):
                    nbr.setColor('gray')
                    nbr.setDistance(currentVert.getDistance() + 1)
                    nbr.setPredecesor(currentVert)
                    procQueue.enqueue(nbr)
            currentVert.setColor('black')

    def traverse(self, startKey, endKey):
        self.breadthFirstSearch(startKey)
        result = [endKey]
        vert = self.verts[endKey]
        reached = False
        while vert.getPredecesor() != None:
            result.append(vert.getPredecesor().getId())
            vert = vert.getPredecesor()
            if vert.getId() == startKey:
                reached = True
                break
        if not reached:
            raise Empty(f'Vertex {endKey} is unreachable from vertex {startKey}')
        result.reverse()
        return result