from peewee import *
import ignore


db = MySQLDatabase("Wikilinks", user='root', passwd=ignore.password_string)