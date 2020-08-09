from bs4 import BeautifulSoup as beautiful_soup

class SoupWrapper:

    def __init__(self, content):
        self.soup = beautiful_soup(content, 'lxml', from_encoding='utf-8')

    def get_tag_soups(self, tag):
        result_set_soup = self.soup.select(tag)
        tag_soups = []

        for soup in result_set_soup:
            tag_soup = TagWrapper(soup)
            tag_soups.append(tag_soup)

        return tag_soups

class TagWrapper:

    def __init__(self, tag_soup):
        self.tag_soup = tag_soup

    def find_tag_soup_with_class(self, tag, css_class):
        new_tag_soup = self.tag_soup.find(tag, class_=css_class)
        return TagWrapper(new_tag_soup)

    def get_text(self):
        return self.tag_soup.text
