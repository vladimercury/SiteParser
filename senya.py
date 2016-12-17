from word_parser import WordParserUtil
from frame import progress
input_file = open('..\website-definition\storage\output\\1481892128922_best\content.data', 'r')
raw_data = input_file.read().splitlines()
output = open('..\website-definition\storage\output\\1481892128922_best\content_removed_stopwords.data', 'w')
num = sum(1 for _ in input_file)
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