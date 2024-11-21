from bs4 import BeautifulSoup
import requests
import re
import matplotlib.pyplot as plt
import numpy as np


array_filters = ["C#", "JAVASCRIPT", "PYTHON", "C++", "C", "C#", "MATLAB", "JAVA", "SQL", "REACT", "ANGULAR", "AZURE"]
filters = {
    
    
    }

URL = "https://www.finn.no/job/fulltime/search.html?industry=65&industry=33&industry=8&location=0.20001&occupation=0.23&occupation=0.22"
FIRST_URL_PART = URL.split("?")[0]

PAGES = []


def getAllPages(url=URL):
    
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    print(FIRST_URL_PART)
    buttons_div = soup.find("div", class_="hidden md:block s-text-link")
    buttons_div_parent = buttons_div.parent
    next_button = buttons_div_parent.find("a", attrs={"rel":"next"})
    print(next_button)
    buttons = buttons_div.contents
    for button in buttons:
        href = button['href']
        if FIRST_URL_PART + href not in PAGES:
            PAGES.append(FIRST_URL_PART + href)
        
        if button.nextSibling == None:
            if next_button == None:
                break
            newUrl = FIRST_URL_PART + href
            getAllPages(newUrl)
    
        
getAllPages()  
def getJobListings(page_number):
    job_listings_urls = []    
    #page_number_url_section = "&page={0}".format(page_number)
    page_url = BASE_URL
    
    page = requests.get(page_url)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    divs = soup.find("div", class_="grid grid-cols-1 md:grid-cols-2 grid-flow-row-dense sf-result-list mt-8 -mx-8") #Divs with job listings
    for div in divs:
        anchor = div.find("a")
        href = anchor.get("href")
        
        if(href):
            job_listings_urls.append(href)
        
    return job_listings_urls
def scrapeJobs(listings):
    count = 0
    for listing in listings:
     url = listing
     page = requests.get(url)
     soup = BeautifulSoup(page.text, 'html.parser')
     
     main = soup.find("main")
     main_div = main.find("div", class_="import-decoration")
     
     paragraphs = main_div.findAll("p")
     count +=1
     print("Working on HTTP request {0}/{1}".format(count, len(listings)))
     for paragraph in paragraphs:
         split_regex = re.split(r'[,\s!?\s]+', paragraph.text)
         if(len(split_regex)<=1):
             continue
         elif(len(split_regex)>1):
             split_regex = ' '.join(split_regex).upper().split()
         
         for filter in array_filters:
            if filter in split_regex:
                
                if filter not in filters:
                    filters[filter] = 0
                filters[filter] +=1
         
   
    
listings = getJobListings(0)
scrapeJobs(listings)
print(filters)
# Extract the counts for the pie chart
y = np.array(list(filters.values()))

# Plot the pie chart
plt.pie(y, labels=list(filters.keys()), autopct='%1.1f%%')
plt.title("Frequency of Programming Languages in Job Listings")
plt.show()
#A single period between each string replacement !!IMPORTANT
#base_url = "https://www.finn.no/job/fulltime/search.html?location={num_locations}.20001{county}{city}" 