class HTMLGetterUtil:
    _charset_regex = '<meta[^>]*?charset=([^"\']+)'
    _headers = {
        'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36'
    }

    @staticmethod
    def _get_response(url, status_len=70):
        import requests
        import sys
        tab_len = 0 if len(url) > status_len else status_len - len(url)
        try:
            response = requests.get(url, HTMLGetterUtil._headers)
            print('GET ' + url + (' ' * tab_len) + '[ OK ]')
            return response
        except requests.ConnectionError:
            print('GET ' + url + (' ' * tab_len) + '[FAIL]', file=sys.stderr)
        return None

    @staticmethod
    def _get_charset(response):
        import re
        encoding = response.encoding
        match = re.search(HTMLGetterUtil._charset_regex, str(response.content))
        if match is not None:
            encoding = match.groups()[0]
        return encoding

    @staticmethod
    def _decode(response):
        charset = HTMLGetterUtil._get_charset(response)
        return response.content.decode(charset)

    @staticmethod
    def get(url):
        response = HTMLGetterUtil._get_response(url)
        if response is not None:
            return HTMLGetterUtil._decode(response)
        return None
