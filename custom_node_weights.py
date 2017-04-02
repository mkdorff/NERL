# I will 8th root the values because it kind of works?

import ignore
import pickle
import math
from peewee import *

with open('node_edge_creation/nodes.pickle', 'rb') as handle:
    nodes = pickle.load(handle)
print("Edge Values loaded...")

count = 0
for key in nodes:
    count += 1
    val = nodes[key]
    nodes[key] = math.sqrt(math.sqrt(math.sqrt(val)))

    if not (count % 50000):
        print(count)

with open('custom_node.pickle', 'wb') as handle:
    pickle.dump(nodes, handle, protocol=pickle.HIGHEST_PROTOCOL)
