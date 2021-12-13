from collections import Counter
import re
from pprint import pprint
import os
from graph import Graph
from graph.visuals import plot_2d
dirname = os.path.dirname(__file__)

data = open(f'{dirname}/07-input.txt').read().split("\n")
data = [m.groups() for d in data if (m := re.match(r'(.*) bags contain (.+)', d))]
data = [(d[0], m.group(2), int(m.group(1))) for d in data for s in d[1].split(',') if (m := re.search(r'(\d+) (\S+ \S+) bag', s))]
g = Graph(from_list=data)
print(sum([g.is_connected(n, 'shiny gold') for n in g.nodes()]))

def contains(this_node):
    count = 0
    for node in g.nodes(from_node=this_node):
        print(this_node, node, g.edge(this_node, node), sep='\t')
        count += g.edge(this_node, node) * (1 + contains(node))
    return count

print(contains('shiny gold'))