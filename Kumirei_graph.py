#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 21:29:27 2121

@author: -Fenrir
"""

import networkx as nx
from matplotlib import pyplot as plt

options = {'node_color': '#8fb2ea',
           'node_size': 1210,
           'width': 1,
           'with_labels': True
           }


def create_graph():
    """ Create a directed graph with 22 nodes. One of the nodes is isolated,
    and all the other nodes have 4 in edges and 4 out edges.
    """
    G = nx.DiGraph()
    G.add_nodes_from(range(21))
    for i in range(21):
        G.add_edge(i, (4 * i + 1) % 21)
        G.add_edge(i, (4 * i + 2) % 21)
        G.add_edge(i, (4 * i + 3) % 21)
        G.add_edge(i, (4 * i + 4) % 21)

    # some manual fixes for nodes pointing towards itself    
    G.remove_edge(6,6)
    G.remove_edge(13,13)
    G.remove_edge(20,20)
    G.add_edge(6,13)
    G.add_edge(13,20)
    G.add_edge(20,6)
    
    G = nx.relabel_nodes(G, lambda x: x + 1)
    G.add_node(0)

    return G


def plot_graph(G):
    """ Given the graph created in create_graph(), divide the nodes into two
    shells and plot the graph.
    """
    plt.figure(figsize=(12,12))
    nx.draw_shell(G, nlist=[[0], range(1,22)], **options)
    plt.savefig("Kumirei_graph.png", dpi=300)
    plt.show()


def main():
    plot_graph(create_graph())


if __name__ == "__main__":
    main()
