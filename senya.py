from word_parser import WordParserUtil
from frame import progress
raw_data = open('senya.txt', 'r').read().splitlines()
output = open('senya_result.txt', 'w')
output.write(raw_data[0] + '\n')
num = int(raw_data[0])
count = 0
for line in raw_data[1:]:
    if line == '':
        continue
    line_data = line.split()
    site = line_data[0]
    words = WordParserUtil.get_stemmed_words_without_stopwords(' '.join(line_data[1:]), lang='russian')
    output.write(site + ' ' + ' '.join(words) + '\n')
    count += 1
    if count % 7 == 1 or count == num:
        progress(count / num)
print()