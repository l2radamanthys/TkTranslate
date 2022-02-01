# -*- coding: utf-8 -*-

try:
    from urllib.request import Request, urlopen  # Python 3
    from urllib.parse import urlencode
except ImportError:
    from urllib2 import Request, urlopen  # Python 2
    from urllib import urlencode
import json
from const import URL, HEADERS


def translate(text, source="es", target="en"):
    params = {"sl": source, "tl": target, "q": text}
    request = Request(URL)
    for key, value in HEADERS:
        request.add_header(key, value)
    data = bytes(urlencode(params).encode())
    try:
        raw_text = urlopen(request, data).read()
        # print(raw_text)
        raw_text = raw_text.decode("utf-8", errors="replace")
        json_ = json.loads(raw_text)
        # return ''.join(map(lambda e: e['trans'], json_['sentences']))
        result = ""
        for e in json_["sentences"]:
            try:
                if "trans" in e:
                    result += e["trans"]
            except UnicodeDecodeError:
                pass
        return result
    except Exception as err:
        print(err)
        return "Error al traducir el texto"


if __name__ == "__main__":
    # test api
    print("hola mundo ->", translate("hola mundo"))
