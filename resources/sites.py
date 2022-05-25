import json
import re
from bs4 import BeautifulSoup
from resources.header import headers
import requests 
from torrequest import TorRequest

DATA = {}
timeout = None

def request(args):
    global timeout
    global session
    try:
        if args.tor:
            session = TorRequest().session
        else:
            session = requests.Session()
        if args.proxy:
           proxy = args.proxy
           session.proxies = {"http": proxy, "https": proxy}
        else:
           session.proxies = None
        if args.browser:
            if args.browser == "chrome":
                browser = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36'}
            if args.browser == "firefox":
                browser = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'}
            else:
                browser = {'user-agent':'Mozilla/5.0'}
            session.headers = browser
    except requests.exceptions.ProxyError as err:
        error = "Proxy Error"
        print(error)

# This is where the link shortcuts start
# It really took me time

class Shorten():
    """Query Status Enumeration.

    Describes status of query about a given username.
    """

    def __init__(self, url):
        """Create Query Result Object.

        Contains information about a specific method of detecting usernames on
        a given type of web sites.
        """
        self.url = url # get long url

                  

    def adfly(self):
        res = session.get(url='https://adf.ly/', timeout=timeout)
        flysessid = str(res.headers['set-cookie']).split(';')[0] + ';'
        html = BeautifulSoup(res.text, 'lxml')
        csrfToken = html.find('input', attrs={'type':'hidden'})['value']

        headers = {'cookie': flysessid}
        data = {'_user_id':'-1', 'url': self.url, 'csrfToken': csrfToken}
        res = session.post(url='https://adf.ly/shortener/shorten', data=data, headers=headers, timeout=timeout)
        try:
            uri = res.json()['shorts'][0]['short_url']
        except IndexError:
            DATA['name'] = 'Adf.ly'
            DATA['url'] = 'No Found!'
            DATA['status'] = 'false'
            json_data = json.dumps(DATA)
            return json_data
        DATA['name'] = 'Adf.ly'
        DATA['url'] = uri
        DATA['status'] = 'true'
        json_data = json.dumps(DATA)
        return json_data



    def binbuck(self):
        bash_url = 'https://www.binbucks.com/site/link'
        data = {
            'link': self.url,
            'directLink': 'false',
            'createPaste': ''
            }
        res = session.post(url=bash_url, data=data, timeout=timeout)
        if res.status_code == 200:
            jsonX = json.loads(res.text)
            jsonZ = jsonX['link']
            DATA['name'] = 'Binbucks'
            DATA['url'] = jsonZ
            DATA['status'] = 'true'
            json_data = json.dumps(DATA)
            return json_data
        else:
            DATA['name'] = 'Binbucks'
            DATA['url'] = 'No Found!'
            DATA['status'] = 'false'
            json_data = json.dumps(DATA)
            return json_data



    def bitly(self):
        url_content = 'https://bitly.com/data/anon_shorten'
        data = {
            'url': self.url
            }
        res = session.post(url_content, data=data, headers=headers, timeout=timeout)
        x = res.text
        y = json.loads(x)
        DATA['name'] = 'Bitly'
        DATA['url'] = y['data']['link']
        DATA['status'] = 'true'
        json_data = json.dumps(DATA)
        return json_data



    def chilp(self):
        bash_link = 'http://chilp.it/go.php'
        data = {'url': self.url}
        res = session.post(url=bash_link, data=data, timeout=timeout)
        soup = BeautifulSoup(res.text, 'html.parser')
        for div in soup.findAll('div', attrs={'class':'ResultYES'}):
            DATA['name'] = 'Chilp'
            DATA['url'] = div.contents[0]
            DATA['status'] = 'true'
            json_data = json.dumps(DATA)
            return json_data



    def clck(self):
        bash_link = 'https://clck.ru/--?json=true&url=' + str(self.url)
        res = session.get(url=bash_link, timeout=timeout)
        DATA['name'] = 'Clck.ru'
        DATA['url'] = res.json()[0]
        DATA['status'] = 'true'
        json_data = json.dumps(DATA)
        return json_data



    def cleanuri(self):
        bash_link = 'https://cleanuri.com/api/v1/shorten'
        data = {'url': self.url}
        res = session.post(bash_link, data=data, timeout=timeout)
        DATA['name'] = 'Cleanuri'
        DATA['url'] = res.json()['result_url']
        DATA['status'] = 'true'
        json_data = json.dumps(DATA)
        return json_data



    def cpmlink(self):
        res_1 = session.get(url='https://cpmlink.net/', timeout=timeout)
        content = res_1.text
        html = BeautifulSoup(content, "lxml")
        csrf = html.find('input', {'name':'token', 'type':'hidden'})['value']
        url_content = 'https://cpmlink.net/shorten.php'
        data = {'token': csrf, 'url': self.url}
        res_2 = session.post(url=url_content, data=data, timeout=timeout)
        jsonL = res_2.content
        jsonX = json.loads(jsonL)
        jsonZ = jsonX['slug']
        jsonB = 'https://cpmlink.net/' + jsonZ
        DATA['name'] = 'Cpmlink'
        DATA['url'] = jsonB
        DATA['status'] = 'true'
        json_data = json.dumps(DATA)
        return json_data



    def cuttly(self):
        url_content = 'https://cutt.ly/scripts/shortenUrl.php'
        data = {
            'url': self.url,
            }
        res = session.post(url_content, data=data, timeout=timeout)
        DATA['name'] = 'Cuttly'
        DATA['url'] = res.text
        DATA['status'] = 'true'
        json_data = json.dumps(DATA)
        return json_data



    def cuttus(self):
        res = session.get('https://cutt.us/')
        soup = BeautifulSoup(res.text, "lxml")
        link = soup.find('input', {'type':'text', 'name':'txt_name', 'id':'txt_name', 'class':'required'})['value']
        data = {'txt_url': self.url, 'txt_name': link}
        res = session.post('https://cutt.us/processreq.php', data=data, timeout=timeout)
        DATA['name'] = 'Cutt.us'
        DATA['url'] = 'https://cutt.us/' + link
        DATA['status'] = 'true'
        json_data = json.dumps(DATA)
        return json_data



    def gcc(self):
        res_1 = session.get(url='https://gcc.gl/', timeout=timeout)
        content = res_1.text
        html = BeautifulSoup(content, "lxml")
        csrf = html.find('input', {'type':'hidden', 'name':'airport_csrf_token'})['value']
        head = {
            'Cookie': 'airport_csrf='+csrf+';'
            }
        url_content = 'https://gcc.gl/panel/create_short'
        data = {
            'airport_csrf_token': csrf,
            'urlOrigin': self.url,
            'urlCustom': '',
            'urlPassword': '' ,
            'urlNote': '',
            'urlRedirect': 'accept'
            }
        res_2 = session.post(url=url_content, data=data, headers=head, timeout=timeout)
        a = res_2.text
        HTTP = BeautifulSoup(a, "lxml")
        z = HTTP.find('input', {'type':'text', 'class':'form-control', 'id':'result', 'placeholder':''})['value']
        DATA['name'] = 'Gcc.gl'
        DATA['url'] = z
        DATA['status'] = 'true'
        json_data = json.dumps(DATA)
        return json_data



    def gg(self):
        bash_url = 'http://gg.gg/create'
        data = {
            'custom_path':'',
            'long_url': self.url
            }
        res = session.post(url=bash_url, data=data, timeout=timeout)
        content = res.text
        DATA['name'] = 'Gg.gg'
        DATA['url'] = content
        DATA['status'] = 'true'
        json_data = json.dumps(DATA)
        return json_data



    def gitio(self):
        bash_url = 'https://git.io/create'
        data = {
            'url': self.url
            }
        res = session.post(url=bash_url, data=data, timeout=timeout)
        g = 'https://git.io/' + res.text
        if res.status_code == 200:
            DATA['name'] = 'Git.io'
            DATA['url'] = g
            DATA['status'] = 'true'
            json_data = json.dumps(DATA)
            return json_data
        if res.status_code == 500:
            DATA['name'] = 'Git.io'
            DATA['url'] = 'No Found!'
            DATA['status'] = 'false'
            json_data = json.dumps(DATA)
            return json_data



    def ibitly(self):
        data = {"provider":"t.ly","long_url": self.url,"domain":"https://ibit.ly/"}
        res = session.post('https://t.ly/api/v1/link/shorten', data=data, timeout=timeout)
        URL = json.loads(res.text)['short_url']
        DATA['name'] = 'Ibit.ly'
        DATA['url'] = URL
        DATA['status'] = 'true'
        json_data = json.dumps(DATA)
        return json_data



    def intip(self):
        payload = {'uri': self.url}
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'}
        response = session.post('https://intip.in/+intip', data=payload, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        uri = 'https://intip.in' + str(soup.find('script').contents[0]).split('=')[1].replace(' ','').replace('"','').replace(';','').replace('+','')
        DATA['name'] = 'Intip'
        DATA['url'] = uri
        DATA['status'] = 'true'
        json_data = json.dumps(DATA)
        return json_data       


    def isgd(self):
        data = {
            'url': self.url
            }
        res = session.post(url='https://is.gd/create.php', data=data, timeout=timeout)
        content = res.text
        html = BeautifulSoup(content, "lxml")
        try:
            URL = html.find('input', {'type':'text', 'class':'tb', 'id':'short_url'})['value']
        except:
            DATA['name'] = 'Is.gd'
            DATA['url'] = 'No Found!'
            DATA['status'] = 'false'
            json_data = json.dumps(DATA)
            return json_data
        DATA['name'] = 'Is.gd'
        DATA['url'] = URL
        DATA['status'] = 'true'
        json_data = json.dumps(DATA)
        return json_data



    def linkfox(self):
        bash_url = 'https://linkfox.io/shorten'
        data = {
            'url': self.url,
            'type': 'direct',
            'multiple': '0'
            }
        res = session.post(url=bash_url, data=data, timeout=timeout)
        content = res.text
        jsonZ = json.loads(content)
        JsonX = jsonZ['short']
        DATA['name'] = 'Linkfox'
        DATA['url'] = JsonX
        DATA['status'] = 'true'
        json_data = json.dumps(DATA)
        return json_data



    def linkmngr(self):
        bash_url = 'https://linkmngr.com/wp-json/linkmngr/shorten'
        data = {
            'longlink': self.url
            }
        res = session.post(url=bash_url, data=data, timeout=timeout)
        content = res.text
        jsonZ = json.loads(content)
        JsonX = jsonZ['link']
        DATA['name'] = 'Linkmngr'
        DATA['url'] = JsonX
        DATA['status'] = 'true'
        json_data = json.dumps(DATA)
        return json_data



    def linkshortner(self):
        payload = {'url': self.url}
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'}
        response = session.post('https://linkshortner.net/shorten', data=payload, headers=headers)
        uri = response.json()['data']['shorturl']
        DATA['name'] = 'Linkshortner'
        DATA['url'] = uri
        DATA['status'] = 'true'
        json_data = json.dumps(DATA)
        return json_data



    def n9(self):
        payload = {
            'xjxfun':'create',
            'xjxargs[]': 'S<![CDATA[{}]]>'.format(self.url[0])
        }
        response = session.post('https://n9.cl/ar?l=index.php&l=ar', data=payload)
        soup = BeautifulSoup(response.text, 'html.parser')
        uri = str(soup.find('cmd').contents[0]).split('=')[1].replace(' ','').replace('"','').replace(';','')
        DATA['name'] = 'N9.cl'
        DATA['url'] = uri
        DATA['status'] = 'true'
        json_data = json.dumps(DATA)
        return json_data



    def osdb(self):
        bash_url = 'http://osdb.link/'
        data = {
            'url': self.url
            }
        res = session.post(url=bash_url, data=data, timeout=timeout)
        content = res.text
        html = BeautifulSoup(content, "html.parser")
        x = html.find_all('label', {'id':'surl'})
        email = x[0].contents
        z = email[2]
        DATA['name'] = 'Osdblink'
        DATA['url'] = z
        DATA['status'] = 'true'
        json_data = json.dumps(DATA)
        return json_data



    def ouoio(self):
        res_1 = session.get(url='https://ouo.io/')
        content = res_1.text
        html = BeautifulSoup(content, "lxml")
        csrf = html.find('input', {'name':'_token', 'type':'hidden'})['value']
        url_content = 'https://ouo.io/shorten'
        data = {
            '_token': csrf,
            'url': self.url
            }
        res_2 = session.post(url=url_content, data=data, timeout=timeout)
        jsonL = res_2.text
        jsonX = json.loads(jsonL)
        jsonZ = jsonX['slug']
        jsonB = 'https://ouo.io/' + jsonZ
        DATA['name'] = 'Ouo'
        DATA['url'] = jsonB
        DATA['status'] = 'true'
        json_data = json.dumps(DATA)
        return json_data



    def shortam(self):
        bash_url = 'https://short.am/short_home.php'
        data = {
            'myUrl': self.url
            }
        res = session.post(bash_url, data=data, timeout=timeout)
        DATA['name'] = 'Shortam'
        DATA['url'] = res.text
        DATA['status'] = 'true'
        json_data = json.dumps(DATA)
        return json_data
    


    def shortest(self):
        url_content = 'https://shorte.st/shortener/shorten'
        data = {
            'url': self.url
            }
        res = session.post(url_content, data=data, timeout=timeout)
        x = res.text
        y = json.loads(x)
        DATA['name'] = 'Shortentest'
        DATA['url'] = y['shortenedUrl']
        DATA['status'] = 'true'
        json_data = json.dumps(DATA)
        return json_data



    def shortmy(self):
        payload = {'urls': self.url, 'expire':''}
        response = session.post('https://shortmy.link/', data=payload, timeout=1)
        soup = BeautifulSoup(response.text, 'lxml')
        uri = soup.find('input', attrs={'type':'text', 'class':'form-control shortened-url-input'})['value']
        DATA['name'] = 'Shortmy'
        DATA['url'] = uri
        DATA['status'] = 'true'
        json_data = json.dumps(DATA)
        return json_data



    def shorturl(self):
        payload = {'u': self.url}
        res = session.post(url='https://www.shorturl.at/shortener.php', data=payload, timeout=timeout)
        content = res.text
        html = BeautifulSoup(content, "lxml")
        DE = html.find('input', {'type':'text'})['value']
        URL = 'https://www.' + DE
        DATA['name'] = 'Shorturl'
        DATA['url'] = URL
        DATA['status'] = 'true'
        json_data = json.dumps(DATA)
        return json_data



    def snip(self):
        payload = {"url": self.url,"cta_message":"Sign up and customize the CTA!","button_url":"https://sniply.io/pricing/"}
        res = session.post('https://snip.ly/pub/snip', data=payload, timeout=timeout)
        uri = res.json()['snip_url']
        DATA['name'] = 'Sniply'
        DATA['url'] = uri
        DATA['status'] = 'true'
        json_data = json.dumps(DATA)
        return json_data



    def tinyurl(self):
        url_content = "http://tinyurl.com/api-create.php"
        data_payload = {
            'url': self.url,
            }
        res = session.post(url_content, data=data_payload, timeout=timeout)
        DATA['name'] = 'Tinyurl'
        DATA['url'] = res.text
        DATA['status'] = 'true'
        json_data = json.dumps(DATA)
        return json_data



    def tly(self):
        data = {"long_url": self.url}
        res = session.post('https://t.ly/api/v1/link/shorten', data=data, timeout=timeout)
        URL = json.loads(res.text)['short_url']
        DATA['name'] = 'Tly'
        DATA['url'] = URL
        DATA['status'] = 'true'
        json_data = json.dumps(DATA)
        return json_data



    def trimurl(self):
        bash_url = 'https://trimurl.co/index.php/shorten/create'
        data = {
            'url': self.url
            }
        res = session.post(url=bash_url, data=data, timeout=timeout)
        if res.status_code == 200:
            content = res.text
            a = re.split(r'\s',content)
            f = a[0]
            DATA['name'] = 'Trimurl'
            DATA['url'] = f
            DATA['status'] = 'true'
            json_data = json.dumps(DATA)
            return json_data
        if res.status_code == 403:
            DATA['name'] = 'Trimurl'
            DATA['url'] = 'No Found!'
            DATA['status'] = 'false'
            json_data = json.dumps(DATA)
            return json_data



    def twtr(self):
        data = {"provider":"t.ly","long_url": self.url,"domain":"https://twtr.to/"}
        res = session.post('https://t.ly/api/v1/link/shorten', data=data, timeout=timeout)
        URL = json.loads(res.text)['short_url']
        DATA['name'] = 'Twtr.to'
        DATA['url'] = URL
        DATA['status'] = 'true'
        json_data = json.dumps(DATA)
        return json_data



    def u(self):
        payload = {'url': self.url, 'from':'', 'a': 'add'}
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'}
        response = session.post("https://u.to/", data=payload, headers=headers)
        uri = response.text.split('=')[-1].split('>')[1].replace('</a','')
        DATA['name'] = 'U.to'
        DATA['url'] = uri
        DATA['status'] = 'true'
        json_data = json.dumps(DATA)
        return json_data
        


    def urlz(self):
        bash_url = 'https://urlz.fr/'
        data = {
            'url': self.url,
            }
        res = session.post(url=bash_url, data=data, timeout=timeout)
        content = res.text
        html = BeautifulSoup(content, "lxml")
        uri = html.find('input', attrs={'type':'text', 'id':'url', 'name':'url'})['value']
        DATA['name'] = 'Urlz.fr'
        DATA['url'] = uri
        DATA['status'] = 'true'
        json_data = json.dumps(DATA)
        return json_data



    def vgd(self):
        payload = {'url': self.url}
        response = session.post('https://v.gd/create.php', data=payload, timeout=timeout)
        html = BeautifulSoup(response.text, "lxml")
        try:
            uri = html.find('input', {'type':'text', 'class':'tb', 'id':'short_url'})['value']
        except:
            DATA['name'] = 'V.gd'
            DATA['url'] = 'No Found!'
            DATA['status'] = 'false'
            json_data = json.dumps(DATA)
            return json_data
        DATA['name'] = 'V.gd'
        DATA['url'] = uri
        DATA['status'] = 'true'
        json_data = json.dumps(DATA)
        return json_data



    def vht(self):
        response = session.get('https://v.ht/processreq.php', timeout=1)
        soup = BeautifulSoup(response.text, "lxml")
        txt_name = soup.find('input', {'type':'text', 'name':'txt_name', 'id':'txt_name', 'class':'required'})['value']
        #
        payload = {'txt_url': self.url, 'txt_name': txt_name}
        response = session.post('https://v.ht/processreq.php', data=payload, timeout=1)
        DATA['name'] = 'V.ht'
        DATA['url'] = 'https://v.ht/' + txt_name
        DATA['status'] = 'true'
        json_data = json.dumps(DATA)
        return json_data



    def vu(self):
        payload = {'url': self.url}
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0'}
        response = session.post('https://vu.fr/shorten', data=payload, headers=headers)
        uri = response.json()['data']['shorturl']
        DATA['name'] = 'Vu.fr'
        DATA['url'] = uri
        DATA['status'] = 'true'
        json_data = json.dumps(DATA)
        return json_data



    def wiki(self):
        substring = "wikipedia.org"
        if substring in self.url:
            bash_url = 'https://meta.wikimedia.org/w/api.php'
            data = {
                'action': 'shortenurl',
                'format': 'json',
                'url': self.url
                }
            res = session.post(url=bash_url, data=data, timeout=timeout)
            content = res.text
            jsonX = json.loads(content)
            jsonZ = jsonX['shortenurl']['shorturl']
            DATA['name'] = 'Wikipedia'
            DATA['url'] = jsonZ
            DATA['status'] = 'true'
            json_data = json.dumps(DATA)
            return json_data
        else:
            DATA['name'] = 'Wikipedia'
            DATA['url'] = 'No Found!'
            DATA['status'] = 'false'
            json_data = json.dumps(DATA)
            return json_data



    def youtube(self):
        substring = "https://www.youtube.com/watch?v="
        if substring in self.url:
            bash_url = 'https://y2u.be/create.php'
            data = {'URL': self.url}
            res = session.post(url=bash_url, params=data, timeout=timeout)
            content = res.text
            html = BeautifulSoup(content, "lxml")
            z = html.findAll('input', {'onclick':'this.focus();this.select()', 'type':'text', 'class':'url', 'readonly':'readonly'})[1]['value']
            DATA['name'] = 'YouTube'
            DATA['url'] = z
            DATA['status'] = 'true'
            json_data = json.dumps(DATA)
            return json_data
        else:
            DATA['name'] = 'YouTube'
            DATA['url'] = 'No Found!'
            DATA['status'] = 'false'
            json_data = json.dumps(DATA)
            return json_data



    def zzb(self):
        url_content = 'http://zzb.bz/panel/short/add_short'
        data = {
            'urlOrigin': self.url,
            'urlCustom':'',
            'urlPassword':'' ,
            'urlDescription': ''
            }
        res = session.post(url=url_content, data=data, timeout=timeout)
        content = res.text
        html = BeautifulSoup(content, "lxml")
        z = html.find('input', {'type':'text', 'id':'url', 'name':'urlOrigin'})['value']
        DATA['name'] = 'Zzb'
        DATA['url'] = z
        DATA['status'] = 'true'
        json_data = json.dumps(DATA)
        return json_data
