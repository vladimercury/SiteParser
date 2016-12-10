from html_parser import HTMLParserUtil
import re
a = ['http://www.windowsphone.com/s?appid=bf257862-b1a9-43c7-a3ab-d85c69270f9f',
     'http://w?e',
     'https://news.mail.ru/currency.html?type=lme&code=OIL2#lme',
     'http://aspirantura.ifmo.ru/?main=44']

for i in a:
    x = re.search(HTMLParserUtil._link_regex, i)
    if x is not None:
        print(x.group())