from coordDistance import coordDist

def weightDef(graph,src,dest,i,alpha):
    ''' Definition of the Weights - 'i' corresponts to the index identifying
    the destination node among the source's children '''
    comf = graph.edges[src][1][i][0]
    risk = graph.edges[src][1][i][1]
    weight = (1-alpha)*comf + alpha*risk
    return weight

def bfs_paths(graph, start, goal, alpha):
    ''' Breath first path search - weighted'''
    minWeight = 10**7
    best_path, visited, viswght = [], [start], [0]
    queue = [(start, [start], 0)] # vertex, path, weight
    while queue:
        (vertex, path, weight) = queue.pop(0)
        for i in range(len(graph.childrenOf(vertex))):
            child = graph.childrenOf(vertex)[i]
            newWeight = weight + weightDef(graph,vertex,child,i,alpha)
            if child in visited:
                if viswght[visited.index(child)] < newWeight:
                    continue
                else: viswght[visited.index(child)] = newWeight
            elif child not in visited:
                visited.append(child), viswght.append(newWeight)
            if newWeight < minWeight:
                if child == goal:
                    minWeight = newWeight
                    best_path = path[:]
                    best_path.append(child)
                elif child not in path:
                    newpath = path[:]
                    newpath.append(child)
                    queue.append((child,newpath,newWeight))
    return best_path, minWeight
    
def pathSegment(graph,latList,lonList,start,end,alpha):
    ''' Where start and end are lists: [lat,lon] '''
    # searching start and end nodes
    startDists = []
    endDists = []
    for i in range(len(latList)):
        startDists.append(coordDist(start[0],start[1],latList[i],lonList[i]))
        endDists.append(coordDist(end[0],end[1],latList[i],lonList[i]))
    startInd = startDists.index(min(startDists))
    endInd = endDists.index(min(endDists))
    startNode = graph.nodes[startInd]
    endNode = graph.nodes[endInd]
    
    # running BFS
    best, totalWeight = bfs_paths(graph, startNode, endNode, alpha)

    comfort = 0
    risk = 0
    for i in range(len(best))[:-1]:
        src = best[i]
        dest = best[i+1]
        ind = graph.edges[src][0].index(dest)
        comfort += graph.edges[src][1][ind][0]
        risk += graph.edges[src][1][ind][1]

    return best, totalWeight, comfort, risk