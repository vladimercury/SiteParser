from word_parser import WordParserUtil
from frame import progress
import sys
reload(sys)
sys.setdefaultencoding('utf8')

raw_data = open('../website-definition/storage/output/1481986676099/simpletest.txt', 'r').read().splitlines()
output = open('../website-definition/storage/output/1481986676099/content_removed_stopwords.data', 'w')
output.write(raw_data[0] + '\n')
num = int(raw_data[0])
count = 0
for line in raw_data[1:]:
    if line == '':
        continue
    line_data = line.split()
    site = line_data[0]
    words = WordParserUtil.get_stemmed_words_without_stopwords(' '.join(line_data[1:]))
    output.write(site + ' ' + ' '.join(words) + '\n')
    count += 1
    if count % 7 == 1 or count == num:
        progress(count / num)
print()