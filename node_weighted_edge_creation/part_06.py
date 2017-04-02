import ignore
import pickle
from peewee import *

with open('norm_nodes.pickle', 'rb') as handle:
    norm_nodes = pickle.load(handle)
print("Normalized Edge Values loaded...")

db = MySQLDatabase('Wikilinks', user='root', passwd=ignore.password_string, charset='utf8mb4')
class LongTextField(TextField):
    db_field = 'longtext'
class Page(Model):
    title = CharField()
    links = LongTextField()

    class Meta:
        database = db
db.connect()
nodes = {}

# 2500001-3000000

for x in range(2500001, 3000001):
    current_page = Page.select().where(Page.id == x).get()
    current_links = current_page.links.split("###")

    for node in current_links:
        weight = norm_nodes[node]
        if node in nodes:
            nodes[node] += (1 * weight)
        else:
            nodes[node] = (1 * weight)

    if not x % 50000:
        print(x)

with open('nodes_06.pickle', 'wb') as handle:
    pickle.dump(nodes, handle, protocol=pickle.HIGHEST_PROTOCOL)