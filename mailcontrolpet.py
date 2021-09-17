import imaplib

import email
import string
import time
import urllib2
import subprocess
global user
global password
global PrintToScreen 
global smtp_server
global smtp_user
global smtp_pass
global EmailPhoto
global SensorNumber
global SendEmails
import sys
import smtplib
from lxml import html
import os, glob, time, operator
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

from email.parser import HeaderParser

SensorNumber = 306

def get_latest_photo(files):
    lt = operator.lt
    if not files:
        return None
    now = time.time()
    latest = files[0], now - os.path.getctime(files[0])
    for f in files[1:]:
        age = now - os.path.getctime(f)
        if lt(age, latest[1]):
            latest = f, age
    return latest[0]

def BuildMessage(SensorNumber):
        # Routine to fetch the location and zone descriptions from the server  
        messagestr =''        
        #RecordSet = GetDataFromHost(6,[SensorNumber])
        #if PrintToScreen: print RecordSet
        #if RecordSet==False:
            #return  
        #zonedesc=RecordSet[0][0]
        #locationdesc = RecordSet[0][1]
        #messagestr="This is your requested picture"
        return messagestr


smtp_server="smtp.gmail.com"    # usually something like smtp.yourisp.com or smtp.gmail.com or smtp.mail.yahoo.com
smtp_user="faplpet@gmail.com"      # usually the main email address of the account holder
smtp_pass="CatsandDogs"
IMAP_SERVER='imap.gmail.com'
IMAP_PORT=993

emailr = []

try:
 M1=imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
 M=imaplib.IMAP4_SSL(IMAP_SERVER )
 M.login('faplpet@gmail.com', 'CatsandDogs')
 M.select()
 print "login "







 emailr=[]
 print "test"
 type, data = M.search(None, '(TEXT "")' )

 Status = "a not armed"
 if os.path.isfile ("/etc/armed"):
    Status = "a armed"

 print '1'
 j = 0
 num=0
 for num in data[0].split():
    print 'num',num
    type, data = M.fetch(num,'(RFC822.SIZE BODY[HEADER.FIELDS (FROM)])')
    M.store( num, '+FLAGS', '\\Deleted' )
    message = data[0][1]
    message = message[6:]
    string.replace(message,'<','')
    string.replace(message,'>','')
    string.replace(message,' ','')
    i = 0
    print message
    type, data = M.fetch(num, '(RFC822)')
    msgbody = data[0][1]
    temp =email.message_from_string(msgbody)
    print temp.get_content_type()
    if temp.get_content_type() == "text/plain":
        name =  temp.get_payload( decode=True)
    if temp.get_content_maintype()=='multipart':  
        for payload in temp.walk():
            print payload.get_content_type()+ "l"
            #for p in payload.get_payload():
                #print p.get_payload(decode=True)
            if payload.get_content_type() == "text/html":
                temper= html.fromstring(payload.get_payload(decode=True))
                print payload.get_payload()
                name =  temper.text_content()
            if payload.get_content_type() == "text/plain":
                name=payload.get_payload(decode=True)
                print 'hi'
        #else:
            #print temp.get_payload(decode=True)
    #print temp.get_payload(decode=True)
    
    #quit() 
    start = name.find("Message")
    if start > 0:
       name = name[start+7:]
    start = name.find("</TITLE" )
    if start > 0:
       name = name[start+7:] 
    end = msgbody.find("message")
    #print start, end
    name = name.strip()
    print name,name
    #quit()

    
    #message = message[i+1:]

    #i = 0
    #while message[i]!='>':
       #i=i+1
       #print message[i]



    #print message

    
    #message = message[:i-1]
    emailr.append(message)
    


 

    
    Status = ""
    found = 0
    fp = open( '/home/pi/petsms/pet.log' )
    for line in fp:
        if line.find(name.upper()) != -1:
            Status = Status + line
            found = 1
    if found == 0:
        Status = "We could not find a match for " + name + ".  Check your spelling or they may not be in the system yet."


    tmp2 = "ALL"
    tmp1 = name.upper()
    print ("hi")
    print (tmp1)
    print (tmp2)


    if tmp1 == tmp2:
        Status = "Follow the link below. It will give you a list of all of the pets currently in the petfinder system.  Click on the pet you are interested in to get their full biography. \n http://fpm.petfinder.com/petlist/petlist.cgi?shelter=OH166&limit=400&style=10&"

    i = 0
    while i < len(emailr):
                # Define email addresses to use
                addr_to   = emailr[i]
                addr_from = smtp_user

                                 
                msg = MIMEText(Status) 
            
                addr_to   = emailr[i]
                #addr_from = 'faplpet@gmail.com"
                msg['To']   = addr_to 
                msg['From'] = addr_from
                msg['Subject'] = "Fapl Pet Information"
                #msg.preamble = 'Multipart message.\n'  
                #part = MIMEText(msgtext) 
                #msg.attach(part)
                print "To", addr_to
                print addr_from
                print Status
               
               


                s = smtplib.SMTP()#_SSL(smtp_server, 465)
                s.connect("smtp.gmail.com",587)
                s.ehlo()
                s.starttls()
                s.login(smtp_user,smtp_pass)
                s.sendmail(msg['From'], msg['To'], msg.as_string())
                s.quit()
                #if PrintToScreen: print msg;
                i = i+1



                print "middle 1" 

                type, data = M.fetch(num,'(RFC822.SIZE BODY[HEADER.FIELDS (FROM)])')
                #M.store( num, '+FLAGS', '\\Deleted' )


                #if PrintToScreen: print msg;
                i = i+1



                print "middle 1" 

                type, data = M.fetch(num,'(RFC822.SIZE BODY[HEADER.FIELDS (FROM)])')
                #M.store( num, '+FLAGS', '\\Deleted' )






































 M.expunge()
 M.logout()



except Exception, e:
 print e
