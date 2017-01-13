import codecs
def parse_first():
    input_data = open('..\\linked_lda\\model\\single\\model-test-2.inf.twords', 'r').read().splitlines()
    result = []
    topics = []
    topic = None
    for line in input_data:
        if line.startswith('\t'):
            poss = line.split()
            topics.append((poss[0], float(poss[1])))
        else:
            if topic is not None:
                result.append((topic, topics))
                topics = list()
            topic = line
    result.append((topic, topics))
    return result


def parse_second():
    input_data = open('..\\linked_lda\\model\\single\\model-test-2.inf.theta', 'r').read().splitlines()
    result = {}
    for line in input_data:
        split = line.split()
        result[int(split[0])] = list(map(float, split[1:]))
    return result


def parse_third():
    input_data = codecs.open('..\\website-definition\\website-download\\storage\\output\\1484290824065\\indexed.mapping.data',
        'r', encoding='utf8').read().splitlines()
    result = {}
    for line in input_data:
        split = line.split()
        result[int(split[0])] = split[1]
    return result


themes = parse_first()
sites_themes = parse_second()
sites = parse_third()

out = codecs.open('output/themes_out.txt', 'w', encoding='utf8')

for key in sites_themes:
    if key == 0:
        continue
    theme = max(range(len(sites_themes[key])), key=lambda x: sites_themes[key][x])
    out.write(' '.join([sites[key]] + [x[0] for x in themes[theme][1]]) + '\n')
out.close()