# coding=utf-8
class WordParserUtil:
    _lang_symbols = {
        'russian': 'а-яё',
        'english': 'a-z'
    }

    @staticmethod
    def get_all_words(text, lang='english'):
        import re
        regex = '[^' + WordParserUtil._lang_symbols[lang] + ']+'
        lower = text.lower()
        filter_regex = re.split(regex, lower)
        return [x for x in filter_regex if len(x) > 1]

    @staticmethod
    def get_stemmed_words(text, lang='english'):
        import nltk
        words = WordParserUtil.get_all_words(text, lang)
        stemmer = nltk.stem.snowball.SnowballStemmer(lang)
        return [stemmer.stem(word) for word in words]

    @staticmethod
    def get_stemmed_words_without_stopwords(text, lang='english'):
        import nltk
        words = WordParserUtil.get_stemmed_words(text, lang)
        stopwords = nltk.corpus.stopwords.words(lang)
        return [word for word in words if word not in stopwords]
