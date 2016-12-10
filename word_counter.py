class WordCounterUtil:
    @staticmethod
    def count(words):
        import collections
        return sorted(collections.Counter(words).items(), key=lambda x: x[1], reverse=True)
