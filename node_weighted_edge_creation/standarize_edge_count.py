import pickle

with open('../node_edge_creation/nodes.pickle', 'rb') as handle:
    nodes = pickle.load(handle)

print("Read nodes from pickle...")

# Straight from mysql
mean = 14.2156
stddev = 328.59654013327895

for key in nodes:
    nodes[key] = (nodes[key] - mean) / stddev


print("Write total nodes to pickle...")
with open('norm_nodes.pickle', 'wb') as handle:
    pickle.dump(nodes, handle, protocol=pickle.HIGHEST_PROTOCOL)