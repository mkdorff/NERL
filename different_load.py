import page as page_node
import pickle
import re
import csv
import pandas as pd


def format_links(text):
    if '|' in text:
        text = text[:text.index('|')]
    if '#' in text:
        text = text[:text.index('#')]
    if text[0].islower():
        text = text.capitalize()
    return text


page_text = ''
in_page = False
pages = []
printed = 0

with open("/Volumes/Ampharos/Wikipedia/enwiki-20170301-pages-articles.xml") as infile:
    for line in infile:
        if in_page:
            page_text += line
            if '</page>' in line:
                in_page = False
                if '<redirect' in page_text:
                    continue

                title = re.search('<title>(.*)</title>', page_text).group(1)

                page_text = re.sub('(\]\])', ']]\n', page_text)
                page_text = [x for x in re.findall('\[\[(.*)\]\]', page_text)
                             if not (x.startswith('Category:') or x.startswith('Wikipedia:') or x.startswith('File:') or
                                     x.startswith('#') or x.startswith('Project:') or x.startswith('WP:') or
                                     x.startswith('Special:') or x.startswith('User talk:') or x.startswith('S:') or
                                     x.startswith('MOS:') or x.startswith('User:') or
                                     x.startswith('wikt:') or x.startswith('|') or x.startswith(':') or len(x) == 0)]
                links = [format_links(x) for x in page_text]

                temp_thing = [title] + links

                pages.append(temp_thing)
                if not (len(pages) % 10000):
                    print(len(pages))
                continue
        elif '<page>' in line:
            if '</page>' in line:
                pages.extend([line])  # I don't think this happens so... error checking nope
                continue
            in_page = True
            page_text = ''
            page_text += line
            continue

        if len(pages) == 3:
            break

pandaed = pd.DataFrame(pages)
pandaed.to_csv('csv_links.csv', index=False, header=False)



# with open('csv_links.csv', 'w') as myfile:
#     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#     wr.writerow(pages)


#
# with open('wiki_links.pickle', 'wb') as f:
#     pickle.dump(pages, f)


# kind of the last of my worries rn
# new_list = [x for x in pages if not '<redirect' in x]
# print(pages[1].links)
