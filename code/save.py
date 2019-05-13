from StreetGraph import *
import os,pickle # cPickle in python 2

def saveGraph(graph,filename='/code/graph_files/WeightedGraph1.txt'):
    savefile = open(os.path.dirname(os.getcwd()) + filename, 'wb')
    pickle.dump(graph, savefile, pickle.HIGHEST_PROTOCOL)
    savefile.close()