import os

choice = raw_input("Enter 1 to paste a link, 2 to do a YouTube search : ")

if choice == '1':
	os.system("python writing_link.py")
elif choice == '2':
	os.system("python finding_link.py")
else:
	print("Didn't you read properly ? now run the script once again silly !")

