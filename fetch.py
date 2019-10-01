import requests, lxml.html
import PyPDF2
from datetime import datetime, timedelta
import re
import glob, os
import json

def getinf():
    # Get the previous URL number from website - News coverage section
    response = requests.get('https://jmfl.com/media-center/news-announcements')
    html = lxml.html.fromstring(response.content)
    curr_link = str(html.xpath('//*[@id="C003_Col00"]/div[3]/div[2]/div/div[1]/div[2]/div/div[2]/div[1]/a/@href'))
    url_no = re.findall(r'\d+', curr_link)
    url_no = int(url_no[0])
    print(url_no)


    # Get list of PDF files in the directory
    os.chdir('C:\\Users\\ncrasto\\Desktop\\SiteFinUpload')
    lsfiles = glob.glob("*.pdf")
    print('\n', lsfiles)


    time_increment = 0
    data = {}
    data["list"] = []

    for lsfile in lsfiles:
        # Extracts text from the PDF document
        objPath = os.path.join('C:\\Users\\ncrasto\\Desktop\\SiteFinUpload\\'+lsfile)
        pdfObj = open(objPath, 'rb')
        pdfRead = PyPDF2.PdfFileReader(pdfObj)
        pgObj = pdfRead.getPage(0)
        op = pgObj.extractText()
        print(op)

        # Gets the date from the text string and converts it into the date format
        date_str = re.findall(r'\d\d\s\w\w\w\-\d\d', op)
        date = datetime.strptime(date_str[0], '%d %b-%y') + timedelta(hours=13, minutes=20)
        date = date + timedelta(minutes=time_increment)
        date = datetime.strftime(date, '%m/%d/%Y %H:%M')
        # Gets the place of publication from the text string
        place = re.findall(r'\-\s\w+\;', op)
        place = re.sub("[^a-zA-Z]+", " ", place[0])
        print('\nOn',date,'in',place)
        time_increment = time_increment + 60
        url_no = url_no + 1

        # convert the data to json format
        data["list"].append({"title": "lorem ipsum", "filename": lsfile, "urlno": url_no, "place": place, "datetime": date})

    with open('C:\\Users\\ncrasto\\Desktop\\SiteFinUpload\\rawdata.json', 'w') as writefile:
        json.dump(data, writefile, indent=4)


