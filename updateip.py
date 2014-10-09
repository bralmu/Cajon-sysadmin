#!/usr/bin/env python
import ipgetter
import ftplib
import time

while(True):
    print "* Obtaining your external IP"
    myip = ipgetter.myip()
    myaddress = "http://%s:8088/"%(myip)
    print "    Your address is "+myaddress
    filetext = """<html>
    <head>
    <title>Redirecting to Jira</title>
    <script>
    window.location = "%s"
    </script>
    </head>
    <body>
    If you are not redirected click on this link <a href="%s">%s</a>
    </body>
    </html>
    """%(myaddress,myaddress,myaddress)
    file = open("index.html","w")
    file.write(filetext)
    file.close()
    print "    file index.html created"
    print "* Logging to ftp"
    session = ftplib.FTP('madgeargames.com','username','password')
    print "    "+session.pwd()
    session.cwd("/www/jira")
    print "    "+session.pwd()
    print "    uploading file index.html"
    file = open("index.html","rb")
    session.storbinary('STOR index.html', file)
    file.close()
    print "    file uploaded"
    session.quit()
    print "    conection closed"
    print "* Waiting 5 minutes\n\n"
    time.sleep(300)
