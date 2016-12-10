class HTMLParserUtil:
    _link_regex = '^[\w]+://[A-Za-z0-9-]+\.[A-Za-z0-9\./-]+'
    _extracted_tags = [
        'script', 'img', 'link', 'style'
    ]

    @staticmethod
    def get_data(html):
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html, 'html.parser')
        HTMLParserUtil._extract(soup)
        new_soup = BeautifulSoup(soup.prettify(), 'html.parser')
        return new_soup.get_text(), \
               HTMLParserUtil._process_links([link.get('href') for link in new_soup.find_all('a')])

    @staticmethod
    def _process_links(refs):
        import re
        links = set()
        for ref in refs:
            if ref is not None:
                match = re.search(HTMLParserUtil._link_regex, ref)
                if match is not None:
                    links.add(match.group())
        return list(links)

    @staticmethod
    def _extract(soup):
        for tag in HTMLParserUtil._extracted_tags:
            [element.extract() for element in soup(tag)]
        return soup
