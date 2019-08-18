from random import choice
import requests
from bs4 import BeautifulSoup as bs

def get_pr(html):
    soup = bs(html,'lxml')
    trs = soup.find('table',{'id':'proxylisttable'}).find_all('tr')[1:51]

    proxies =[]

    for tr in trs:
        tds = tr.find_all('td')
        ip = tds[0].text.strip()
        port = tds[1].text.strip()
        schema = 'https' if 'yes' in tds[6].text.strip() else 'http'
        proxy = {'schema': schema, 'address': ip + ':' + port}
        proxies.append(proxy)

    return choice(proxies)

def get_htm(url):
    r = requests.get(url)
    return r.text

def get_proxy():
    url = 'https://free-proxy-list.net/'
    pr = get_pr(get_htm(url))
    proxy = {pr['schema']: pr['address']}
    return proxy

if __name__== '__main__':
    get_proxy()

