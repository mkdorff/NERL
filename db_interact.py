import ignore
import re
from peewee import *


def format_links(text):
    if '|' in text:
        text = text[:text.index('|')]
    if '#' in text:
        text = text[:text.index('#')]
    if text[0].islower():
        text = text.capitalize()
    return text


db = MySQLDatabase('Wikilinks', user='root', passwd=ignore.password_string)

class LongTextField(TextField):
    db_field = 'longtext'

class Page(Model):
    title = CharField()
    links = LongTextField()

    class Meta:
        database = db


db.connect()

page_text = ''
in_page = False
pages = []
printed = 0

# Change this
with open("/Users/Mohonri/Desktop/wiki_part01.xml") as infile:
    for line in infile:
        if in_page:
            page_text += line
            if '</page>' in line:
                in_page = False
                if '<redirect' in page_text:
                    continue

                title = re.search('<title>(.*)</title>', page_text).group(1)

                # Puke
                page_text = re.sub('(\]\])', ']]\n', page_text)
                page_text = [x for x in re.findall('\[\[(.*)\]\]', page_text)
                             if not (x.startswith('Category:') or x.startswith('Wikipedia:') or x.startswith('File:') or
                                     x.startswith('#') or x.startswith('Project:') or x.startswith('WP:') or
                                     x.startswith('Special:') or x.startswith('User talk:') or x.startswith('S:') or
                                     x.startswith('MOS:') or x.startswith('User:') or x.startswith('Image:') or
                                     x.startswith('wikt:') or x.startswith('|') or x.startswith(':') or len(x) == 0)]
                links = [format_links(x) for x in page_text]

                Page(title=title, links="###".join(links)).save()

                # print(links)

                temp_thing = [title] + links

                pages.append(temp_thing)

                # if not (len(pages) % 10000):
                #     print(len(pages))
                continue

        elif '<page>' in line:
            if '</page>' in line:
                pages.extend([line])  # I don't think this happens so... error checking nope
                continue
            in_page = True
            page_text = ''
            page_text += line
            continue

        if len(pages) == 20:
            break



