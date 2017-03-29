import re

class Page(object):
    def __init__(self, page_text):
        self.title = re.search('<title>(.*)</title>', page_text).group(1)
        self.links = self.parse_links(page_text)

    def parse_links(self, page_text):
        page_text = re.sub('(\]\])', ']]\n', page_text)
        # Cringe
        page_text = [x for x in re.findall('\[\[(.*)\]\]', page_text)
                     if not (x.startswith('Category:') or x.startswith('Wikipedia:') or x.startswith('File:') or
                             x.startswith('#') or x.startswith('Project:') or x.startswith('WP:') or
                             x.startswith('Special:') or x.startswith('User talk:') or x.startswith('S:') or
                             x.startswith('MOS:') or x.startswith('User:') or
                             x.startswith('wikt:') or x.startswith('|') or x.startswith(':') or len(x) == 0)]
        links = [self.format_links(x) for x in page_text]

        return links

    def format_links(self, text):
        if '|' in text:
            text = text[:text.index('|')]
        if '#' in text:
            text = text[:text.index('#')]
        if text[0].islower():
            text = text.capitalize()
        return text

    def return_array(self):
        return [self.title], self.links