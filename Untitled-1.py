
from bs4 import BeautifulSoup
import requests

html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

soup=BeautifulSoup(html_text,'lxml')
jobby=soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')

for job in jobby:  
    pub=job.find('span', class_= 'sim-posted').span.text
    
    if '5' in pub:     
        company_name=job.find('h3',class_ ='joblist-comp-name').text.replace(' ','')
        skill=job.find('span', class_ ='srp-skills').text.replace(' ','')
        print(f"Company Name:{company_name}")
        print(f" required skill:{skill}")        
           
        print(' ')       
                  
            
           
                