class WordParserUtil:
    @staticmethod
    def _is_rus(word):
        import re
        if re.search('[а-яё]', word) is None:
            return 0
        return 1

    @staticmethod
    def get_all_words(text):
        import re
        lower = text.lower()
        filter_all = re.split('[^a-zа-яё]+', lower)
        return [(x, WordParserUtil._is_rus(x)) for x in filter_all if len(x) > 1]

    @staticmethod
    def get_stemmed_words(text):
        import nltk
        words = WordParserUtil.get_all_words(text)
        stemmers = [nltk.stem.snowball.SnowballStemmer('english'),
                    nltk.stem.snowball.SnowballStemmer('russian')]
        return [stemmers[word[1]].stem(word[0]) for word in words]

    @staticmethod
    def get_stemmed_words_without_stopwords(text):
        import nltk
        words = WordParserUtil.get_stemmed_words(text)
        stopwords = []
        for i in ['russian', 'english']:
            stopwords += nltk.corpus.stopwords.words(i)
        return [word for word in words if word not in stopwords]