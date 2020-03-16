import bs4 as bs
import urllib as u
import os
import webbrowser

source = u.request.urlopen('http://oklahoman.com/article/5656708/those-guys-are-the-new-wave-thunders-shai-gilgeous-alexander-and-knicks-rj-barrett-boosting-canadian-basketball').read()
soup = bs.BeautifulSoup(source,'html.parser')

html =  soup.find_all('body')

path = os.path.abspath('temp.html')
url = 'file:\\' + path

with open(path,'w') as f:
    f.write(str(html))
webbrowser.open(url)
