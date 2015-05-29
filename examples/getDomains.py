#!/usr/bin/env python

# BSides London 2015 - Maltego Magic Template by @catalyst256


import requests
from MaltegoTransform import *


def new_transform(arg):
    m = MaltegoTransform()
    m.parseArguments(arg)
    ip = m.getVar('ipv4-address')
    wrkspc = m.getVar('workspace')
    url = 'http://10.1.99.250:8125/api/v1.0/%s/%s/domains' % (wrkspc, ip)
    try:
        r = requests.get(url)
        j = r.json()
        for i in j['items']:
            ent = m.addEntity('maltego.Domain', i['domain'])
            ent.addAdditionalFields('workspace', 'Workspace ID', True, wrkspc)
            ent.addAdditionalFields('ipaddr', 'IP Address', True, ip)
    except Exception as e:
        m.addUIMessage(str(e))
    m.returnOutput()


if __name__ == '__main__':
    new_transform(sys.argv)

