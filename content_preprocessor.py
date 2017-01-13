from word_parser import WordParserUtil
from frame import progress
import codecs
encoding = 'utf8'
input_path = '../website-definition/website-download/storage/output/1484290824065/indexed.content.data'
output_path = '../website-definition/website-download/storage/output/1484290824065/content_removed_stopwords.data'
raw_data = codecs.open(input_path, 'r', encoding=encoding).read().splitlines()
output = open(output_path, 'w')
num = len(raw_data) - 1
output.write(str(num) + '\n')
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