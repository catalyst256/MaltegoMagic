#!/usr/bin/env python

# BSides London 2015 - Maltego Magic Template by @catalyst256


import requests
from MaltegoTransform import *


def new_transform(arg):
    emails = []
    m = MaltegoTransform()
    m.parseArguments(arg)
    domain = m.getVar('fqdn')
    ip = m.getVar('ipaddr')
    wrkspc = m.getVar('workspace')
    url = 'http://10.1.99.250:8125/api/v1.0/%s/%s/domains' % (wrkspc, ip)
    try:
        r = requests.get(url)
        j = r.json()
        for i in j['items']:
            if domain in i['domain']:
                for x in i['data']['emails']:
                    if x not in emails:
                        emails.append(x)
        for t in emails:
            ent = m.addEntity('maltego.EmailAddress', t)
            ent.addAdditionalFields('workspace', 'Workspace ID', True, wrkspc)
    except Exception as e:
        m.addUIMessage(str(e))
    m.returnOutput()


if __name__ == '__main__':
    # print sys.argv
    new_transform(sys.argv)

