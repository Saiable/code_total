from url_manage import URLManager
import re
class URLExtractor(URLManager):
    def __init__(self):
        self.urls = set()

    def extractor(self, html, regex):

        return self.urls