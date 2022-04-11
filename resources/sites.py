import json
from bs4 import BeautifulSoup
import re
from resources.header import headers
from requests_futures.sessions import FuturesSession



DATA = {}
timeout = 1.0
session = FuturesSession()



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
        res = session.get('https://adf.ly/')
        response = res.result()
        flysessid = str(response.headers['set-cookie']).split(';')[0] + ';'
        html = BeautifulSoup(response.text, 'lxml')
        csrfToken = html.find('input', attrs={'type':'hidden'})['value']

        headers = {'cookie': flysessid}
        data = {'_user_id':'-1', 'url': self.url, 'csrfToken': csrfToken}
        res = session.post('https://adf.ly/shortener/shorten', data=data, headers=headers)
        response = res.result()
        try:
            uri = response.json()['shorts'][0]['short_url']
        except IndexError:
            DATA['name'] = 'Adf.ly'
            DATA['url'] = 'No Found!'
            json_data = json.dumps(DATA)
            return json_data
        DATA['name'] = 'Adf.ly'
        DATA['url'] = uri
        json_data = json.dumps(DATA)
        return json_data



    def binbuck(self):
        bash_url = 'https://www.binbucks.com/site/link'
        data = {
            'link': self.url,
            'directLink': 'false',
            'createPaste': ''
            }
        res = session.post(url=bash_url, data=data)
        response = res.result()
        if response.status_code == 200:
            jsonX = json.loads(response.text)
            jsonZ = jsonX['link']
            DATA['name'] = 'Binbucks'
            DATA['url'] = jsonZ
            json_data = json.dumps(DATA)
            return json_data
        else:
            DATA['name'] = 'Binbucks'
            DATA['url'] = 'No Found!'
            json_data = json.dumps(DATA)
            return json_data



    def bitly(self):
        url_content = 'https://bitly.com/data/anon_shorten'
        data = {
            'url': self.url
            }
        res = session.post(url_content, data=data, headers=headers)
        response = res.result()
        x = response.text
        y = json.loads(x)
        DATA['name'] = 'Bitly'
        DATA['url'] = y['data']['link']
        json_data = json.dumps(DATA)
        return json_data



    def chilp(self):
        bash_link = 'http://chilp.it/go.php'
        data = {'url': self.url}
        res = session.post(bash_link, data=data)
        response = res.result()
        soup = BeautifulSoup(response.text, 'html.parser')
        for div in soup.findAll('div', attrs={'class':'ResultYES'}):
            DATA['name'] = 'Chilp'
            DATA['url'] = div.contents[0]
            json_data = json.dumps(DATA)
            return json_data



    def clck(self):
        bash_link = 'https://clck.ru/--?json=true&url=' + str(self.url)
        res = session.get(bash_link)
        response = res.result()
        DATA['name'] = 'Clck.ru'
        DATA['url'] = response.json()[0]
        json_data = json.dumps(DATA)
        return json_data



    def cleanuri(self):
        bash_link = 'https://cleanuri.com/api/v1/shorten'
        data = {'url': self.url}
        res = session.post(bash_link, data=data)
        response = res.result()
        DATA['name'] = 'Cleanuri'
        DATA['url'] = response.json()['result_url']
        json_data = json.dumps(DATA)
        return json_data



    def cpmlink(self):
        res_1 = session.get(url='https://cpmlink.net/')
        response_1 = res_1.result()
        content = response_1.text
        html = BeautifulSoup(content, "lxml")
        csrf = html.find('input', {'name':'token', 'type':'hidden'})['value']
        url_content = 'https://cpmlink.net/shorten.php'
        data = {'token': csrf, 'url': self.url}
        res_2 = session.post(url=url_content, data=data)
        response_2 = res_2.result()
        jsonL = response_2.content
        jsonX = json.loads(jsonL)
        jsonZ = jsonX['slug']
        jsonB = 'https://cpmlink.net/' + jsonZ
        DATA['name'] = 'Cpmlink'
        DATA['url'] = jsonB
        json_data = json.dumps(DATA)
        return json_data



    def cuttly(self):
        url_content = 'https://cutt.ly/scripts/shortenUrl.php'
        data = {
            'url': self.url,
            }
        res = session.post(url_content, data=data)
        response = res.result()
        DATA['name'] = 'Cuttly'
        DATA['url'] = response.text
        json_data = json.dumps(DATA)
        return json_data



    def cuttus(self):
        res = session.get('https://cutt.us/')
        response = res.result()
        soup = BeautifulSoup(response.text, "lxml")
        link = soup.find('input', {'type':'text', 'name':'txt_name', 'id':'txt_name', 'class':'required'})['value']
        data = {'txt_url': self.url, 'txt_name': link}
        res = session.post('https://cutt.us/processreq.php', data=data)
        DATA['name'] = 'Cutt.us'
        DATA['url'] = 'https://cutt.us/' + link
        json_data = json.dumps(DATA)
        return json_data



    def gcc(self):
        res_1 = session.get(url='https://gcc.gl/')
        response_1 = res_1.result()
        content = response_1.text
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
        res_2 = session.post(url=url_content, data=data, headers=head)
        response_2 = res_2.result()
        a = response_2.text
        HTTP = BeautifulSoup(a, "lxml")
        z = HTTP.find('input', {'type':'text', 'class':'form-control', 'id':'result', 'placeholder':''})['value']
        DATA['name'] = 'Gccgl'
        DATA['url'] = z
        json_data = json.dumps(DATA)
        return json_data



    def gg(self):
        bash_url = 'http://gg.gg/create'
        data = {
            'custom_path':'',
            'long_url': self.url
            }
        res = session.post(url=bash_url, data=data)
        response = res.result()
        content = response.text
        DATA['name'] = 'Gg.gg'
        DATA['url'] = content
        json_data = json.dumps(DATA)
        return json_data



    def gitio(self):
        bash_url = 'https://git.io/create'
        data = {
            'url': self.url
            }
        res = session.post(url=bash_url, data=data)
        response = res.result()
        g = 'https://git.io/' + response.text
        if response.status_code == 200:
            DATA['name'] = 'Git.io'
            DATA['url'] = g
            json_data = json.dumps(DATA)
            return json_data
        if response.status_code == 500:
            DATA['name'] = 'Git.io'
            DATA['url'] = 'No Found!'
            json_data = json.dumps(DATA)
            return json_data



    def ibitly(self):
        data = {"provider":"t.ly","long_url": self.url,"domain":"https://ibit.ly/"}
        res = session.post('https://t.ly/api/v1/link/shorten', data=data)
        response = res.result()
        URL = json.loads(response.text)['short_url']
        DATA['name'] = 'Ibit.ly'
        DATA['url'] = URL
        json_data = json.dumps(DATA)
        return json_data



    def isgd(self):
        data = {
            'url': self.url
            }
        res = session.post(url='https://is.gd/create.php', data=data)
        response = res.result()
        content = response.text
        html = BeautifulSoup(content, "lxml")
        URL = html.find('input', {'type':'text', 'class':'tb', 'id':'short_url'})['value']
        DATA['name'] = 'Isgd'
        DATA['url'] = URL
        json_data = json.dumps(DATA)
        return json_data



    def linkfox(self):
        bash_url = 'https://linkfox.io/shorten'
        data = {
            'url': self.url,
            'type': 'direct',
            'multiple': '0'
            }
        res = session.post(url=bash_url, data=data)
        response = res.result()
        content = response.text
        jsonZ = json.loads(content)
        JsonX = jsonZ['short']
        DATA['name'] = 'Linkfox'
        DATA['url'] = JsonX
        json_data = json.dumps(DATA)
        return json_data



    def linkmngr(self):
        bash_url = 'https://linkmngr.com/wp-json/linkmngr/shorten'
        data = {
            'longlink': self.url
            }
        res = session.post(url=bash_url, data=data)
        response = res.result()
        content = response.text
        jsonZ = json.loads(content)
        JsonX = jsonZ['link']
        DATA['name'] = 'Linkmngr'
        DATA['url'] = JsonX
        json_data = json.dumps(DATA)
        return json_data



    def osdb(self):
        bash_url = 'http://osdb.link/'
        data = {
            'url': self.url
            }
        res = session.post(url=bash_url, data=data)
        response = res.result()
        content = response.text
        html = BeautifulSoup(content, "html.parser")
        x = html.find_all('label', {'id':'surl'})
        email = x[0].contents
        z = email[2]
        DATA['name'] = 'Osdb'
        DATA['url'] = z
        json_data = json.dumps(DATA)
        return json_data



    def ouoio(self):
        res_1 = session.get(url='https://ouo.io/')
        response_1 = res_1.result()
        content = response_1.text
        html = BeautifulSoup(content, "lxml")
        csrf = html.find('input', {'name':'_token', 'type':'hidden'})['value']
        url_content = 'https://ouo.io/shorten'
        data = {
            '_token': csrf,
            'url': self.url
            }
        res_2 = session.post(url=url_content, data=data)
        response_2 = res_2.result()
        jsonL = response_2.text
        jsonX = json.loads(jsonL)
        jsonZ = jsonX['slug']
        jsonB = 'https://ouo.io/' + jsonZ
        DATA['name'] = 'Ouo'
        DATA['url'] = jsonB
        json_data = json.dumps(DATA)
        return json_data



    def shortam(self):
        bash_url = 'https://short.am/short_home.php'
        data = {
            'myUrl': self.url
            }
        res = session.post(bash_url, data=data)
        response = res.result()
        DATA['name'] = 'Shortam'
        DATA['url'] = response.text
        json_data = json.dumps(DATA)
        return json_data
    


    def shortest(self):
        url_content = 'https://shorte.st/shortener/shorten'
        data = {
            'url': self.url
            }
        res = session.post(url_content, data=data)
        response = res.result()
        x = response.text
        y = json.loads(x)
        DATA['name'] = 'Shortentest'
        DATA['url'] = y['shortenedUrl']
        json_data = json.dumps(DATA)
        return json_data



    def shorturl(self):
        data = {
            'u': self.url
            }
        res = session.post(url='https://www.shorturl.at/shortener.php', data=data)
        response = res.result()
        content = response.text
        html = BeautifulSoup(content, "lxml")
        DE = html.find('input', {'type':'text'})['value']
        URL = 'https://www.' + DE
        DATA['name'] = 'Shorturl'
        DATA['url'] = URL
        json_data = json.dumps(DATA)
        return json_data



    def snip(self):
        payload = {"url": self.url,"cta_message":"Sign up and customize the CTA!","button_url":"https://sniply.io/pricing/"}
        res = session.post('https://snip.ly/pub/snip', data=payload)
        response = res.result()
        uri = response.json()['snip_url']
        DATA['name'] = 'Snip.ly'
        DATA['url'] = uri
        json_data = json.dumps(DATA)
        return json_data



    def tinyurl(self):
        url_content = "http://tinyurl.com/api-create.php"
        data_payload = {
            'url': self.url,
            }
        res = session.post(url_content, data=data_payload)
        response = res.result()
        DATA['name'] = 'Tinyurl'
        DATA['url'] = response.text
        json_data = json.dumps(DATA)
        return json_data



    def tly(self):
        data = {"long_url": self.url}
        res = session.post('https://t.ly/api/v1/link/shorten', data=data)
        response = res.result()
        URL = json.loads(response.text)['short_url']
        DATA['name'] = 'Tly'
        DATA['url'] = URL
        json_data = json.dumps(DATA)
        return json_data



    def trimurl(self):
        bash_url = 'https://trimurl.co/index.php/shorten/create'
        data = {
            'url': self.url
            }
        res = session.post(url=bash_url, data=data)
        response = res.result()
        if response.status_code == 200:
            content = response.text
            a = re.split(r'\s',content)
            f = a[0]
            DATA['name'] = 'Trimurl'
            DATA['url'] = f
            json_data = json.dumps(DATA)
            return json_data
        if response.status_code == 403:
            DATA['name'] = 'Trimurl'
            DATA['url'] = 'No Found!'
            json_data = json.dumps(DATA)
            return json_data



    def twtr(self):
        data = {"provider":"t.ly","long_url": self.url,"domain":"https://twtr.to/"}
        res = session.post('https://t.ly/api/v1/link/shorten', data=data)
        response = res.result()
        URL = json.loads(response.text)['short_url']
        DATA['name'] = 'Twtr.to'
        DATA['url'] = URL
        json_data = json.dumps(DATA)
        return json_data



    def urlz(self):
        bash_url = 'https://urlz.fr/'
        data = {
            'url': self.url,
            }
        res = session.post(url=bash_url, data=data)
        response = res.result()
        content = response.text
        html = BeautifulSoup(content, "lxml")
        uri = html.find('input', attrs={'type':'text', 'id':'url', 'name':'url'})['value']
        DATA['name'] = 'Urlz.fr'
        DATA['url'] = uri
        json_data = json.dumps(DATA)
        return json_data



    def v(self):
        url_content = 'https://v.gd/create.php'
        data = {
            'url': self.url
            }
        res = session.post(url=url_content, data=data)
        response = res.result()
        content = response.text
        html = BeautifulSoup(content, "lxml")
        z = html.find('input', {'type':'text', 'class':'tb', 'id':'short_url'})['value']
        DATA['name'] = 'Vgd'
        DATA['url'] = z
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
            res = session.post(url=bash_url, data=data)
            response = res.result()
            content = response.text
            jsonX = json.loads(content)
            jsonZ = jsonX['shortenurl']['shorturl']
            DATA['name'] = 'Wikipedia'
            DATA['url'] = jsonZ
            json_data = json.dumps(DATA)
            return json_data
        else:
            DATA['name'] = 'Wikipedia'
            DATA['url'] = 'No Found!'
            json_data = json.dumps(DATA)
            return json_data



    def y2u(self):
        substring = "https://www.youtube.com/watch?v="
        if substring in self.url:
            bash_url = 'https://y2u.be/create.php'
            data = {'URL': self.url}
            res = session.post(url=bash_url, params=data)
            response = res.result()
            content = response.text
            html = BeautifulSoup(content, "lxml")
            z = html.findAll('input', {'onclick':'this.focus();this.select()', 'type':'text', 'class':'url', 'readonly':'readonly'})[1]['value']
            DATA['name'] = 'YouTube'
            DATA['url'] = z
            json_data = json.dumps(DATA)
            return json_data
        else:
            DATA['name'] = 'YouTube'
            DATA['url'] = 'No Found!'
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
        res = session.post(url=url_content, data=data)
        response = res.result()
        content = response.text
        html = BeautifulSoup(content, "lxml")
        z = html.find('input', {'type':'text', 'id':'url', 'name':'urlOrigin'})['value']
        DATA['name'] = 'Zzb'
        DATA['url'] = z
        json_data = json.dumps(DATA)
        return json_data