import os

f = open('youtube_links.txt', 'w')

link = raw_input("Paste your link : ")

f.write(link)
f.write('\n')   	

f.close()

os.system("python yt_dwn_play.py")

