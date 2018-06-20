from bs4 import BeautifulSoup
import requests
url=raw_input("Enter Website: ")
r=requests.get("http://"+url)
data=r.txt()
print data
soup=BeautifulSoup(data)
for link in soup.findall('a')
	print link.get('href')
