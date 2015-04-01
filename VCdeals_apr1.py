from bs4 import BeautifulSoup

import requests

#url = raw_input("Enter a website to extract the URL's from: ")

url="http://www.vccircle.com"
arr=[]
i=0
for i in range(0,10):
	r  = requests.get(url+"/deals-venture-capital?page="+str(i))
	data = r.text

	soup = BeautifulSoup(data)
	soup=soup.find('div',{'class':'view-venture-capital-landing'})

	for link in soup.find_all('div',{'class':'view-content'}):
		#dum=link.find('span',{'class':'date-display-single'})
		#print(dum)	
		for l in (link.find_all('a')):
			arr.append(url+l['href'])



for a in arr:
	r=requests.get(a)
	data=r.text
	soup = BeautifulSoup(data)
	print(str(arr.index(a)+1)+".  " + soup.find('h3').text.encode('utf-8')+"\n"+soup.find('p').text.encode('utf-8')+"\n"+a+"\n\n")
