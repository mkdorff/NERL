import ignore
import pickle
from peewee import *

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

# 4000001-4500000

for x in range(4000001, 4500001):
    current_page = Page.select().where(Page.id == x).get()
    current_links = current_page.links.split("###")

    for node in current_links:
        if node in nodes:
            nodes[node] += 1
        else:
            nodes[node] = 1

    if not x % 50000:
        print(x)

with open('nodes_09.pickle', 'wb') as handle:
    pickle.dump(nodes, handle, protocol=pickle.HIGHEST_PROTOCOL)