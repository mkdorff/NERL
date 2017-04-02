import ignore
import pickle
from peewee import *
from collections import Counter

with open('../node_weighted_edge_creation/weighted_nodes.pickle', 'rb') as handle:
    weighted_nodes = pickle.load(handle)
print("Weighted Nodes Loaded...")

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

node_related_links = {}

# 2500001-3000000

for x in range(2500001, 3000001):
    current_page = Page.select().where(Page.id == x).get()
    current_links = current_page.links.split("###")
    related_links = {}
    related_links_list = []

    for node in current_links:
        if node in weighted_nodes:
            related_links[node] = weighted_nodes[node]
        else:
            print("missed: " + node)

        if node in node_id:
            id = node_id[node]
        else:
            continue

    for item in Counter(related_links).most_common(5):
        related_links_list.append(item[0])

    node_related_links[current_page.title] = related_links_list

    if not x % 50000:
        print(x)

with open('nodes_06.pickle', 'wb') as handle:
    pickle.dump(node_related_links, handle, protocol=pickle.HIGHEST_PROTOCOL)