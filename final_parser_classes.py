def parse_first():
    input_data = open('..\\linked_lda\\model\\final\\model\\model-test-2-40.twords', 'r').read().splitlines()
    result = []
    topics = []
    topic = None
    has_class = None
    for line in input_data:
        if line.startswith('\t'):
            poss = line.split()
            topics.append((poss[0], float(poss[1])))
        else:
            if topic is not None:
                result.append((topic, has_class, topics))
                topics = list()
            split = line.split()
            topic = ' '.join(split[:-1])
            has_class = split[-1]
    result.append((topic, topics))
    return result


def parse_second():
    input_data = open('..\\linked_lda\\model\\final\\model\\model-test-2-40.theta', 'r').read().splitlines()
    result = {}
    for line in input_data:
        split = line.split()
        result[int(split[0])] = list(map(float, split[1:]))
    return result


def parse_third():
    input_data = open('..\\website-definition\\website-download\\storage\\output\\last\\indexed.mapping.data', 'r').read().splitlines()
    result = {}
    for line in input_data:
        split = line.split()
        result[int(split[0])] = split[1]
    return result


themes = parse_first()
sites_themes = parse_second()
sites = parse_third()

out = open('classes_out.txt', 'w')

for key in sites_themes:
    theme = max(range(len(sites_themes[key])), key=lambda x: sites_themes[key][x])
    out.write(sites[key]+ ' ' + themes[theme][1] + '\n')
out.close()