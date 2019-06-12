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


def print_neighbors(G, i):
    """ Given a graph and an index, print a dictionary containing the
    neighbors it points toward.
    """
    return G[i]
    

def create_graph():
    """ Create a directed graph with 22 nodes. One of the nodes is isolated,
    and all the other nodes have 4 in edges and 4 out edges.
    """
    G = nx.DiGraph()
    G.add_nodes_from(range(1,22))
    for i in range(1, 22):
        G.add_edge(i, i % 21 + 1)
        G.add_edge(i, (i+1) % 21 + 1)
        G.add_edge(i, (i+2) % 21 + 1)
        G.add_edge(i, (i+3) % 21 + 1)
    G.add_node(0)
    return G


def plot_graph(G):
    """ Given the graph created in create_graph(), divide the nodes into three
    shells and plot the graph.
    """
    plt.figure(figsize=(9,9))
    nx.draw_shell(G, nlist=[[0], range(1,8), range(8,22)], **options)
    plt.savefig("Kumirei_graph.eps")
    plt.show()


def main():
    plot_graph(create_graph())


if __name__ == "__main__":
    main()
