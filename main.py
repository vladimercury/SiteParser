from html_getter import HTMLGetterUtil
from html_parser import HTMLParserUtil
from word_parser import WordParserUtil
sites = open('sites.list', 'r').read().splitlines()
sites_links = open('sites_links.txt', 'w')
sites_words = open('sites_words.txt', 'w')
for site in sites:
    html = HTMLGetterUtil.get(site)
    if html is None:
        continue
    text, links = HTMLParserUtil.get_data(html)
    words = WordParserUtil.get_stemmed_words_without_stopwords(text, 'russian')
    sites_links.write(site + ' ' + ' '.join(links) + '\n')
    sites_words.write(site + ' ' + ' '.join(words) + '\n')
sites_links.close()
sites_words.close()
