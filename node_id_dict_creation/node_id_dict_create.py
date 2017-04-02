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

node_id = {}
max_id = Page.select(fn.MAX(Page.id)).scalar()

for x in range(max_id):
    current_page = Page.select().where(Page.id == x+1).get()
    node_id[current_page.title] = current_page.id

    if not x % 10000:
        print(x)

with open('nodes_01.pickle', 'wb') as handle:
    pickle.dump(node_id, handle, protocol=pickle.HIGHEST_PROTOCOL)