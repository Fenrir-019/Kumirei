#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 19:29:27 2019

@author: -Fenrir
"""

import networkx as nx
from matplotlib import pyplot as plt

options = {'node_color': '#8fb2ea',
           'node_size': 1200,
           'width': 1,
           'with_labels': True
           }


def get_min_in_node(G):
    """ Given a graph G, return the node with minimum number of in edges.
    Return any of them if there are more than 1 such edges.
    """
    


def create_graph():
    """ Create a directed graph with 22 nodes. One of the nodes is isolated,
    and all the other nodes have 4 in edges and 4 out edges.
    """
    G = nx.DiGraph()
    G.add_nodes_from(range(21))
    for i in range(21):
#        if i % 5 == 0:
        G.add_edge(i, (i+2) % 21)
        G.add_edge(i, (i+4) % 21)
        G.add_edge(i, (i+8) % 21)
        G.add_edge(i, (i+22) % 21)
#    G.add_node(21)
    for i in range(21):
        l = [i]
        l.extend(G[i].keys())
        for key in G[i].keys():
            l.extend(G[key])
        l.sort()
        print i, l
    
    print G.in_edges()
#    for i in range(21):
#        for j in range(21):
#            try:
#                assert nx.shortest_path_length(G, i, j) <= 2
#            except AssertionError:
#                print i, j, nx.shortest_path_length(G, i, j)
#                print G[i]
#                for ele in G[i].keys():
#                    print G[ele]
    return G


def plot_graph(G):
    """ Given the graph created in create_graph(), divide the nodes into three
    shells and plot the graph.
    """
    plt.figure(figsize=(12,12))
    nx.draw_circular(G, **options)
#    nx.draw_shell(G, nlist=[[0], range(1,8), range(8,22)], **options)
#    plt.savefig("Kumirei_graph.png", dpi=300)
    plt.show()


def main():
    plot_graph(create_graph())


if __name__ == "__main__":
    main()
