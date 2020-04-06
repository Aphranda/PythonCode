import time
import requests
import execjs

ts = int(time.time()*1000)
session = requests.session()
data = {
'donotcache': ts,
'username': '123456',
}
req = session.post('https://store.steampowered.com/login/getrsakey/', data=data).json()
mod = req["publickey_mod"]
exp = req["publickey_exp"]
timestamp = req["timestamp"]


with open(r'E:\code\cj.js', encoding='utf-8') as f:
    Jsdata = f.read()

text = execjs.compile(Jsdata).call('test', '123456', mod, exp)
print(text)
headers = {
'Host': 'store.steampowered.com',
'Origin': 'https://store.steampowered.com',
'Referer': 'https://store.steampowered.com/login/?redir=&redir_ssl=1',
'Sec-Fetch-Mode': 'cors',
'Sec-Fetch-Site': 'same-origin',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
'X-Requested-With': 'XMLHttpRequest',
}
ts = int(time.time()*1000)
data = {
'donotcache': ts,
'password': text,
'username': '11111',
'twofactorcode': '',
'emailauth': '',
'loginfriendlyname': '',
'captchagid': '-1',
'captcha_text': '',
'emailsteamid': '',
'rsatimestamp': timestamp,
'remember_login': 'false',
}
req = session.post('https://store.steampowered.com/login/getrsakey/', data=data, headers=headers)
print(req.text)