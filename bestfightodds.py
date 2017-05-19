import bs4 as bs
import urllib.request

url = "https://www.bestfightodds.com/"
sauce = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(sauce, 'lxml')
