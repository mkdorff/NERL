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

# 1500001-2000000

for x in range(1500000, 2000001):
    current_page = Page.select().where(Page.id == x).get()
    nodes[current_page.title] = current_page.id

    if not x % 50000:
        print(x)

with open('nodes_04.pickle', 'wb') as handle:
    pickle.dump(nodes, handle, protocol=pickle.HIGHEST_PROTOCOL)