import pickle

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

print("Let's try to add them all together now! :/")
all_recommendations = {}
all_recommendations.update(nodes_01)
all_recommendations.update(nodes_02)
all_recommendations.update(nodes_03)
all_recommendations.update(nodes_04)
all_recommendations.update(nodes_05)
all_recommendations.update(nodes_06)
all_recommendations.update(nodes_07)
all_recommendations.update(nodes_08)
all_recommendations.update(nodes_09)
all_recommendations.update(nodes_10)
all_recommendations.update(nodes_11)

print("Deleting c_nodes...")
del nodes_01
del nodes_02
del nodes_03
del nodes_04
del nodes_05
del nodes_06
del nodes_07
del nodes_08
del nodes_09
del nodes_10
del nodes_11

print("Write total recommendations to pickle...")
with open('highest_recommendations_8_root.pickle', 'wb') as handle:
    pickle.dump(all_recommendations, handle, protocol=pickle.HIGHEST_PROTOCOL)


# meow = {
#     "cat": 4,
#     "cat1": 3,
#     "ca22t": 5.7,
#     "ca1t": 4,
#     "ca2t": 4
# }
#
# yeasd = meow.values()
#
# print("meow")