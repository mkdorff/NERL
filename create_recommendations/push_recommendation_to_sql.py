import pickle
import ignore
from peewee import *

with open('lowest_recommendations.pickle', 'rb') as handle:
    recommendations = pickle.load(handle)
print("Loaded data from pickle...")

db = MySQLDatabase('Wikilinks', user='root', passwd=ignore.password_string, charset='utf8mb4')

class LongTextField(TextField):
    db_field = 'longtext'

class CustomRecommendations(Model):
    title = LongTextField()
    recommendation_01 = LongTextField()
    recommendation_02 = LongTextField()
    recommendation_03 = LongTextField()
    recommendation_04 = LongTextField()
    recommendation_05 = LongTextField()

    class Meta:
        database = db

db.connect()
# db.create_tables([CustomRecommendations])


# FIIIIIIXXXXX

count = 0
for key in recommendations:
    count += 1
    record = CustomRecommendations(title=key)

    # kind of like a case switch with fall through.
    if len(recommendations[key]) > 4:
        record.recommendation_05 = recommendations[key][4]

    if len(recommendations[key]) > 3:
        record.recommendation_04 = recommendations[key][3]

    if len(recommendations[key]) > 2:
        record.recommendation_03 = recommendations[key][2]

    if len(recommendations[key]) > 1:
        record.recommendation_02 = recommendations[key][1]

    if len(recommendations[key]) > 0:
        record.recommendation_01 = recommendations[key][0]

    record.save()

    if not (count % 50000):
        print(count)
