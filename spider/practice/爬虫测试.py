import requests
import parsel


url = "https://m.weibo.cn/status/4476215110667389"

headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36",
        }
response = requests.get(url, headers=headers)
html = response.content.decode('utf-8')
print(html)
data = parsel.Selector(html)