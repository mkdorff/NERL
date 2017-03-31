import ignore
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
# db.create_tables([Page])
# AFTER creation, go to my sql work bench and change links to utf8mb4




# pages = Page.select().where(Page.title=="Alabama").get()

for page in Page.select().where(Page.id == 35):
    links_list = page.links.split("###")

print("meow")

# This works! :D
#Don't look up in sql as we're adding edge count values. Literally... will take 1900 years