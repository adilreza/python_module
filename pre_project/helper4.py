from urllib.request import urlopen
from bs4 import BeautifulSoup
address = 'https://en.wikipedia.org/wiki/Facebook'
page=urlopen(address)

soup = BeautifulSoup(page, 'html.parser')
final=soup.string
print(final)