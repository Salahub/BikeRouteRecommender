import os

def generateConf(filestreets = '/datasets/streets/Zurich_w1_graphPoints.txt', \
    filerisks = '/datasets/bicyclerisk/Zurich_w1_RoadNodeRisk.csv',\
    comfortfnc = 'yes', filecomfort = '', fnccomfort = '/code/comfortCalc.py',\
    buildgraph = 'no', graphfile = '/code/graph_files/WeightedGraph1.txt',\
    mapfilename = '/img/map.gif', mapcoords = [8.5141,8.5523,47.3650,47.3886]):
    
    path = os.path.dirname(os.getcwd())
    f = open(path + '/conf/datacompilation.txt', 'w')
    f.write('filestreets' + '\t' + filestreets + '\n')
    f.write('filerisks' + '\t' + filerisks + '\n')
    f.write('comfortfnc' + '\t' + comfortfnc + '\n')
    f.write('filecomfort' + '\t' + filecomfort + '\n')
    f.write('fnccomfort' + '\t' + fnccomfort + '\n')
    f.write('buildgraph' + '\t' + buildgraph + '\n')
    f.write('graphfile' + '\t' + graphfile + '\n')
    f.write('mapfilename' + '\t' + mapfilename + '\n')
    f.write('mapcoords' + '\t' + str(mapcoords) + '\n')
    f.close()