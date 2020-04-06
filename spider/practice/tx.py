import requests
import re


url = 'https://v.qq.com/x/cover/jg2a5feze5bryj2/j0855hsr5y8.html'
headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    }
response = requests.get(url, headers=headers)
response.encoding = 'utf-8'
html = response.text
print(html)
