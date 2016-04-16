from bs4 import BeautifulSoup as bs
import requests
r = requests.get("http://ocw.mit.edu/courses/sloan-school-of-management/")
data = r.text
soup = bs(data)
courses = []
download_links = []
for link in soup.find_all('a',attrs={'class' : 'preview'}):
    courses.append("http://ocw.mit.edu/{0}/download-course-materials".format(link.get('href')))
for d in courses:
    r = requests.get(d)
    data = r.text
    soup = bs(data)
    for link in soup.find_all('a', attrs={'class' : 'downloadNowButton'}):
        download_links.append("http://ocw.mit.edu/{0}".format(link.get("href")))
        
    
