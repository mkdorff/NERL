import ignore
import re
from peewee import *


def check_link(text, type):
    if type == 'title':
        regex = re.compile('^Category:|^Wikipedia:|^File:|^Template:|^portal|\(disamb[iı]guation\)')
        if re.match(regex, text):
            return True

    if type == 'text':
        regex = re.compile('^Category:|^Wikipedia:|^File:|^#|^Project:|^WP:|^Special:|^User talk:|^S:|^MOS:|'
                           '^User:|^Image:|^User_talk:|^Meta:|^wikt:|^\||^:|^Help:|^Template:|^Toollabs:|^D:|^C:'
                           '|^Commons:|^He:|^Tools:|^Module:|^Wiktionary:|^Talk')
        if re.match(regex, text):
            return True
    return False


def format_links(text):
    if '|' in text:
        text = text[:text.index('|')]
    if '#' in text:
        text = text[:text.index('#')]
    if text[0].islower():
        text = text.capitalize()
    return text


db = MySQLDatabase('Wikilinks', user='root', passwd=ignore.password_string, charset='utf8mb4')

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
printed = 0

# Change this
with open("/Users/Mohonri/Desktop/ccc.xml") as infile:
    for line in infile:
        if in_page:
            page_text += line
            if '</page>' in line:
                in_page = False
                if '<redirect' in page_text:
                    continue

                title = re.search('<title>(.*)</title>', page_text).group(1)
                if check_link(title, type='title'):
                    continue

                # Less Puke
                page_text = re.sub('(\]\])', ']]\n', page_text)
                page_text = [x for x in re.findall('\[\[(.*)\]\]', page_text)
                             if not (check_link(x, type='text') or len(x) == 0)]
                links = [format_links(x) for x in page_text]

                Page(title=title, links="###".join(links)).save()

                printed += 1
                if not (printed % 1000):
                    print(printed)
                continue

        elif '<page>' in line:
            if '</page>' in line:
                pages.extend([line])  # I don't think this happens so... error checking nope
                continue

            in_page = True
            page_text = ''
            page_text += line
            continue