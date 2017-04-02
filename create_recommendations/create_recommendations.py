import ignore
import pickle
from peewee import *
from collections import Counter

# import time

with open('../node_weighted_edge_creation/weighted_nodes.pickle', 'rb') as handle:
    weighted_nodes = pickle.load(handle)
print("Weighted Nodes Loaded...")

# with open('node_edge_creation/nodes.pickle', 'rb') as handle:
#     weighted_nodes = pickle.load(handle)
# print("Nodes Loaded...")

with open('../node_id_dict_creation/nodes_id.pickle', 'rb') as handle:
    node_id = pickle.load(handle)
print("Node IDs Loaded...")

db = MySQLDatabase('Wikilinks', user='root', passwd=ignore.password_string, charset='utf8mb4')
class LongTextField(TextField):
    db_field = 'longtext'
class Page(Model):
    title = CharField()
    links = LongTextField()

    class Meta:
        database = db
db.connect()

# nodes = {}

for x in range(1, 6):

    # start_time = time.time()

    current_page = Page.select().where(Page.id == x+1).get()
    current_links = current_page.links.split("###")
    related_links = {}

    for node in current_links:
        if node in weighted_nodes:
            related_links[node] = weighted_nodes[node]
        else:
            print("missed: " + node)

        if node in node_id:
            id = node_id[node]
        else:
            continue

        # inner_page = Page.select().where(Page.id == id).get()
        # inner_links = inner_page.links.split("###")
        #
        # for innerNode in inner_links:
        #     if innerNode in weighted_nodes:
        #         related_links[innerNode] = weighted_nodes[innerNode]
        #     else:
        #         print("missed: " + innerNode)

    # print("--- %s seconds ---" % (time.time() - start_time))

    # print(list(reversed(Counter(related_links).most_common()))[1:12])
    print(Counter(related_links).most_common(7)[4][0])

        # if node in nodes:
        #     nodes[node] += 1
        # else:
        #     nodes[node] = 1



#       1- 500000
#  500001-1000000
# 1000001-1500000
# 1500001-2000000
# 2000001-2500000
# 2500001-3000000
# 3000001-3500000
# 3500001-4000000
# 4000001-4500000
# 4500001-5000000
# 5000001-5538056

# So interesting note is that when we go two deep, we get United states, NYT, Animal