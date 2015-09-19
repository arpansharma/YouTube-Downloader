import os

with open("youtube_links.txt", 'r') as b:
	j= b.readline()
	j = j.rstrip()
	s1 = "youtube-dl -F "
	s2 = str(j)
	s3 = s1 + s2 

	os.system(s3) 

	b.close()

	choice = raw_input("Enter format code by looking above : ")
	s11 = "youtube-dl -f "
	s4 = s11 + choice + " " + j
	os.system(s4)	

