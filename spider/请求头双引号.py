import re


headers_str = """
:authority: cnzz.mmstat.com
:method: GET
:path: /9.gif?abc=1&rnd=1289630919
:scheme: https
accept: image/webp,image/apng,image/*,*/*;q=0.8
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
cookie: cna=t316FsaLalUCAbcONyI8ha8B; sca=da93af55; atpsida=a6c518c33cb86d878ede0b49_1580722548_10
referer: https://m.gufengmh8.com/manhua/woshizhizhuyouzenyang/1211110.html
sec-fetch-mode: no-cors
sec-fetch-site: cross-site
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36

"""


pattern = '^(.*?): (.*)$'

for line in headers_str.splitlines():
    print(re.sub(pattern, '\'\\1\': \'\\2\', ', line))