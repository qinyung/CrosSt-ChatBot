import requests
import urllib
def qingyunke(msg):
    url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg={}'.format(urllib.parse.quote(msg))
    html = requests.get(url)
    return html.json()["content"]
res = qingyunke(str(input('>')))
print("青云客>>", res)
