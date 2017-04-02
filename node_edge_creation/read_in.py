import pickle
from collections import Counter

# Hahahaha, why didn't I make this a list? Whatever

with open('nodes_01.pickle', 'rb') as handle:
    nodes_01 = pickle.load(handle)

print("Node 01 Read...")

with open('nodes_02.pickle', 'rb') as handle:
    nodes_02 = pickle.load(handle)

print("Node 02 Read...")

with open('nodes_03.pickle', 'rb') as handle:
    nodes_03 = pickle.load(handle)

print("Node 03 Read...")

with open('nodes_04.pickle', 'rb') as handle:
    nodes_04 = pickle.load(handle)

print("Node 04 Read...")

with open('nodes_05.pickle', 'rb') as handle:
    nodes_05 = pickle.load(handle)

print("Node 05 Read...")

with open('nodes_06.pickle', 'rb') as handle:
    nodes_06 = pickle.load(handle)

print("Node 06 Read...")

with open('nodes_07.pickle', 'rb') as handle:
    nodes_07 = pickle.load(handle)

print("Node 07 Read...")

with open('nodes_08.pickle', 'rb') as handle:
    nodes_08 = pickle.load(handle)

print("Node 08 Read...")

with open('nodes_09.pickle', 'rb') as handle:
    nodes_09 = pickle.load(handle)

print("Node 09 Read...")

with open('nodes_10.pickle', 'rb') as handle:
    nodes_10 = pickle.load(handle)

print("Node 10 Read...")

with open('nodes_11.pickle', 'rb') as handle:
    nodes_11 = pickle.load(handle)

print("Node 11 Read...")

c_nodes_01 = Counter(nodes_01)
del nodes_01
print("Counter 01 created & Node 01 Deleted...")

c_nodes_02 = Counter(nodes_02)
del nodes_02
print("Counter 02 created & Node 02 Deleted...")

c_nodes_03 = Counter(nodes_03)
del nodes_03
print("Counter 03 created & Node 03 Deleted...")

c_nodes_04 = Counter(nodes_04)
del nodes_04
print("Counter 04 created & Node 04 Deleted...")

c_nodes_05 = Counter(nodes_05)
del nodes_05
print("Counter 05 created & Node 05 Deleted...")

c_nodes_06 = Counter(nodes_06)
del nodes_06
print("Counter 06 created & Node 06 Deleted...")

c_nodes_07 = Counter(nodes_07)
del nodes_07
print("Counter 07 created & Node 07 Deleted...")

c_nodes_08 = Counter(nodes_08)
del nodes_08
print("Counter 08 created & Node 08 Deleted...")

c_nodes_09 = Counter(nodes_09)
del nodes_09
print("Counter 09 created & Node 09 Deleted...")

c_nodes_10 = Counter(nodes_10)
del nodes_10
print("Counter 10 created & Node 10 Deleted...")

c_nodes_11 = Counter(nodes_11)
del nodes_11
print("Counter 11 created & Node 11 Deleted...")

print("Let's try to add them all together now! :/")

all_nodes = c_nodes_01 + c_nodes_02 + c_nodes_03 + c_nodes_04 + c_nodes_05 + c_nodes_06 + c_nodes_07 + c_nodes_08 + \
            c_nodes_09 + c_nodes_10 + c_nodes_11

print("Deleting c_nodes...")
del c_nodes_01
del c_nodes_02
del c_nodes_03
del c_nodes_04
del c_nodes_05
del c_nodes_06
del c_nodes_07
del c_nodes_08
del c_nodes_09
del c_nodes_10
del c_nodes_11

print("Write total nodes to pickle...")
with open('nodes.pickle', 'wb') as handle:
    pickle.dump(all_nodes, handle, protocol=pickle.HIGHEST_PROTOCOL)