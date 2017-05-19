import bs4 as bs
import urllib.request

url = "https://www.bestfightodds.com/"
class URLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

opener = URLopener()
res = opener.open(url).read()

soup = bs.BeautifulSoup(res, 'lxml')

div = soup.find_all('div', {'class':'table-header'})
children = div[0].findChildren()
x = 0
while x < len(div):
    children = div[x].findChildren()
    for i in range(0,2):
        print(children[i].text)
    x += 1

fighters = soup.find_all('tr', {'class':'even'})
    for n in fighters:
    x = n.find_all('th', {"scope":"row"})
    for n in x:
        print(n.text)

for x range(0,13):
    n = x*4
    print(fighters[n])
    print(fighters[n+1].text)
