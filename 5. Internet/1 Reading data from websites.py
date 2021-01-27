import requests, bs4

url = "https://market.yandex.kz/catalog--smartfony-v-almaty/16814639/list?hid=91491&glfilter=16816262%3A16816264&onstock=1"
r = requests.get(url)
r.encoding = 'UTF8'
b = bs4.BeautifulSoup(r.text, "html.parser")

atitles = b.select("div._1NyIdwOZ6- h3")

for a in atitles:
    print(a.getText())