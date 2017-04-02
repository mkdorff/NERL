import pickle
import ignore
from peewee import *
from collections import Counter

with open('nodes.pickle', 'rb') as handle:
    nodes = pickle.load(handle)

db = MySQLDatabase('Wikilinks', user='root', passwd=ignore.password_string, charset='utf8mb4')

class LongTextField(TextField):
    db_field = 'longtext'

class Nodes(Model):
    title = LongTextField()
    edges = IntegerField()

    class Meta:
        database = db

db.connect()
# db.create_tables([Nodes])
# AFTER creation, go to my sql work bench and change links to utf8mb4

count = 0
for key in nodes:
    count += 1
    if not count % 20000:
        print(count)
    Nodes(title=key, edges=nodes[key]).save()

# print("meow")