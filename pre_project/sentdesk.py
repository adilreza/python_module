import bs4 as bs
import urllib.request
souce = urllib.request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(souce , 'html.parser')
#after converting the html formate this will show the result
# print(soup)
#this will show all page wiht minified version
#print(souce)
#this will show the first p tage in this page
#print(soup.p)
#this will find all paragraph tage in this page
#print(soup.find_all('p'))
for paragraph in soup.find_all('p'):
    #print(paragraph.string) not all string but some string
    print(paragraph.text)