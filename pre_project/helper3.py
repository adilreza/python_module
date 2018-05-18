import bs4 as bs
import pyttsx3
import urllib.request
engine=pyttsx3.init()
souce = urllib.request.urlopen('https://en.wikipedia.org/wiki/china').read()
soup = bs.BeautifulSoup(souce , 'html.parser')
#after converting the html formate this will show the result
# print(soup)
#this will show all page wiht minified version
#print(souce)
#this will show the first p tage in this page
#print(soup.p)
#this will find all paragraph tage in this page
#print(soup.find_all('p'))

res= soup.p
finalres=res.text
engine.say(finalres)
engine.runAndWait()
print(finalres[0:100])