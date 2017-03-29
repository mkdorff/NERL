import page as page_node
import pickle

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

                title, links = page_node.Page(page_text).return_array()

                pages.append((title, links))
                if not (len(pages) % 10000):
                    print(len(pages))
                continue
        elif '<page>' in line:
            if '</page>' in line:
                pages.extend([line]) # I don't think this happens so... error checking nope
                continue
            in_page = True
            page_text = ''
            page_text += line
            continue

        if len(pages) == 100000:
            break

with open('wiki_links.pickle', 'wb') as f:
    pickle.dump(pages, f)


    # kind of the last of my worries rn
# new_list = [x for x in pages if not '<redirect' in x]
# print(pages[1].links)
