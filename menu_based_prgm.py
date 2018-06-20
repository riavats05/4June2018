import datetime
import os
import commands
import webbrowser
import time
import subprocess
x='''
Press1: Check current time and date
Press2: To create a file
Press3: To create a directory
Press4: To search something on google
Press5: To Restart the system
Press6: To shut down the OS
Press7: To check the internet connection on your PC/Laptop
Press8: To check all the connected IPs in your network
Press9: Login whatsapp on Browser
''' 
print x
choice=(int)(raw_input())
if choice==1:
	print "Showing your systems current date and time"
	print datetime.datetime.now()
elif choice==2:
	filename=raw_input("Enter file name with extension:")
	print "Creating a new file on your desktop"
	f=open(filename,'w')
	f.close()
elif choice==3:
	print "Enter the path of your directory"
	dirpath=raw_input()
	print "Creating a new directory on your desktop"
	os.mkdir(path)
elif choice==4:
	msg=raw_input("Enter to search")
	webbrowser.open_new_tab('http://www.google.com/search?q='+msg)
elif choice==5:
	print "Restart the system"
	time.sleep(2)
	os.system("shutdown /r /t 1");
elif choice==6:
	print "Shutting down the system"
	time.sleep(2)
	os.system("shutdown /s /t 1")
elif choice==7:
	print "Checking Internet connection on your PC/Laptop"

elif choice==8:
	print "Checking IPs connected to your network"
	time.sleep(2)
	print commands.getoutput("arp -a | cut -d '(' -f2 | cut -d ')' -f1 ")
elif choice==9:
	print "Log In whatsapp"
else:
	print "Wrong choice"
