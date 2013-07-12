#-------------------------------------------------------------------------------
# Name:        edge_list_reader.py
#
# Purpose:     takes list of edges with voltages from tab delimited
#              .txt file and converts them to a graph with each edge
#               designated as a transformer or transmission line.
#
# Author:      danny duncan
# Created:     11/07/2013
#-------------------------------------------------------------------------------
import numpy as np
from matplotlib import pylab as plt
import networkx as nx
from collections import OrderedDict

def edge_list_reader(readfile):

    # open file
    str_array = []
    color_array = []
    num_lines = sum(1 for line in open(readfile))
    f = open(readfile)
    # copy each line of the file into a list
    for i in range(0,num_lines):
        str_array.append(f.readline())
    # split each list to get rid of white space
    for i in range(0,len(str_array)):
        str_array[i] = str_array[i].split()
    # delete duplicates
    str_array = dict((x[0], x) for x in str_array).values()
    # check to see if voltages differ and label accordingly
    for i in range(0,len(str_array)):
        if str_array[i][3] == str_array[i][2]:
            str_array[i][2] = 'b'
        else:
            str_array[i][2] = 'r'
        str_array[i].pop() # once labeled delete last column
    for i in range(0,len(str_array)):
        color_array.append(str_array[i][2])
    # create graph
    g = nx.Graph()

    # label each edge as transformer or t line
    for i in range(0,len(str_array)):
        g.add_edge(str_array[i][0],str_array[i][1])
        g[str_array[i][0]][str_array[i][1]]['type']=str_array[i][2]
    # DEBUG
    print len(str_array)
    print len(g.edges())
    # draw graph with edges labeled
##    plt.figure(num=None,figsize=(8,6),dpi=120)
##    pos = nx.spring_layout(g)
##    nx.draw(g,pos,with_labels=False,node_size=10)
##    #nx.draw_networkx_edge_labels(g,pos,edge_labels=None,label_pos=0.5,font_size=5)
##    nx.draw_networkx_edges(g,pos,g.edges(),width=6.0,edge_color=color_array)
##    plt.show()

edge_list_reader('C:\\Users\\dunc824\\Documents\\MATLAB\\edges_voltages.txt')
