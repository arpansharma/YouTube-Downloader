import os
import urllib
import urllib2
from bs4 import BeautifulSoup

search = raw_input("Enter your search : ")
textToSearch = search
query = urllib.quote(textToSearch)
url = "https://www.youtube.com/results?search_query=" + query
response = urllib2.urlopen(url)
html = response.read()
soup = BeautifulSoup(html)
f = open('youtube_links.txt', 'w')

for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
	f.write('https://www.youtube.com' + vid['href'])
	f.write('\n')
   	

f.close()
os.system("python yt_dwn_play.py")

