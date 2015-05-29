#!/usr/bin/env python

# BSides London 2015 - Maltego Magic Template by @catalyst256


import requests
from MaltegoTransform import *


def new_transform(arg):
    m = MaltegoTransform()
    url = 'http://10.1.99.250:8125/api/v1.0/%s/ip' % arg
    try:
        r = requests.get(url)
        j = r.json()
        for i in j['items']:
            ent = m.addEntity('maltego.IPv4Address', i['ipaddr'])
            ent.addAdditionalFields('workspace', 'Workspace ID', True, arg)
    except Exception as e:
        m.addUIMessage(str(e))
    m.returnOutput()


if __name__ == '__main__':
    new_transform(sys.argv[1])

