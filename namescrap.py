import os
import string
import commands 

from urllib2 import urlopen

from bs4 import BeautifulSoup

import requests

tmp_string= "test"
while tmp_string.find("Elyria") < 0:
     site = requests.get("http://fpm.petfinder.com/petlist/petlist.cgi?shelter=OH166&haspets=&hasprevious=&title=&limit=200&moreinfo=&style=10&sort=&status=A&picsize=&color1=&color2=&breed=&age=&size=")
     tmp_string = site.text
     
os.system("sudo rm /home/pi/petsms/pettemps.log")
#print site.text

tmplog = open("/home/pi/petsms/pettemps.log", "wb")

sitetext = open("sitetext", "wb")

sitetext.write(site.text)

print 'begin soup'
soup = BeautifulSoup(site.text)
print 'done soup'

image_number = 1
for tag in soup.findAll('img'):
    image_url = tag['src']
    print image_url
    quit
    if image_url.find("cloudfront")>0:
	#print(tag['src'])
        #77 1150
	image_url = image_url[:77] +'1150'
        #image_url = image_url[:70]+'&height=700'
	tmp_string = image_url[43:51]
	#print image_url
        #exit()
	image_number = image_number + 1
        #print tmp_string+'k'
        cat_name="123456789012345678901234567890123451234567890123456789012345678901234"
        while len(cat_name)  > 50:
	   site1 = requests.get("https://www.petfinder.com/petdetail/" + tmp_string)
	   print "http://www.petfinder.com/petdetail/" + tmp_string+"l"
           
          
	   info = site1.text  
           #tmplog.write( info )
           #print info 
           #exit()
          
	   start = info.find("Adopt ")
           diff = 6
	   end = info.find("on Petfinder")
         
           print start, end
           if start < 0 :
              start = info.find("I found " )
              diff = 8
           #quit()          
	   #print info
	   cat_name = info[start+diff:end]
           cat_name = cat_name.replace("&#39;","^")
           cat_name = cat_name.replace("&quot","^")
           cat_name = cat_name.replace(";","")
	   print 'c '+cat_name
          
        
	#info1 = info[end:]
	#start1 = info1.find("clear")
	#end1 = info1.find("<h2>More")
	#cat_description = info1[start1 + 14:end1]
	print cat_name
	tmplog.write(cat_name.upper()  + " http://www.petfinder.com/petdetail/" + tmp_string+"\n")
		
#os.system("sudo cp /home/pi/petsms/pettemps.log /home/pi/petsms/pet.log" );


   
