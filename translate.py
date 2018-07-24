# -*- coding: utf-8 -*-

try:
    from urllib.request import Request, urlopen  # Python 3
    from urllib.parse import urlencode
except ImportError:
    from urllib2 import Request, urlopen  # Python 2
    from urllib import urlencode
import json
from const import URL, HEADERS


def translate(text, source='es', target='en'):
    params = {
        'sl': source, 
        'tl': target, 
        'q': text
    }
    request = Request(URL)
    for key, value in HEADERS:
        request.add_header(key, value)
    data = bytes(urlencode(params).encode())
    try:
        return json.loads(urlopen(request, data).read().decode('utf-8'))['sentences'][0]['trans']
    except:
        return 'Error al traducir el texto'



if __name__ == '__main__':
    # test api
    print('hola mundo ->', translate('hola mundo'))
