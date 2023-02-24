
from bs4 import BeautifulSoup
import requests
import time
print('choose a processor you  want in between AMD and Intel')
processor=input('>')
print('')
print('Enter the company name of which you want to see the laptops of')
cmp=input('>')
print('enter the price point at which you want to see the laptop')
cost=input('>')
print('filtering out the laptops')
def find_laptops():
    html_text=requests.get('https://www.flipkart.com/search?q=laptops&as=on&as-show=on&otracker=AS_Query_TrendingAutoSuggest_4_0_na_na_na&otracker1=AS_Query_TrendingAutoSuggest_4_0_na_na_na&as-pos=4&as-type=TRENDING&suggestionId=laptops&requestId=d5196dca-0e5b-4fc0-8271-c57fd9b74ba3').text
    soup=BeautifulSoup(html_text,'lxml')
    laptops =soup.find_all('div', class_='_2kHMtA')
    with open(f'posts/master_file.txt','w')as f:
    
        for index,laptop in enumerate (laptops):
            company_name=laptop.find('div', class_='_4rR01T').text
            specs=laptop.find('div',class_='fMghEO').text
            price=laptop.find('div',class_='_30jeq3 _1_WHN1').text
            more=str(laptop.a['href'])

            
            try:
                
                    f.write(f"Laptop_name: {company_name.strip()}\n\n")
                    
                    specs=specs.replace('\ufffd'," ")
                    f.write(f"Specs: {specs.strip()}\n\n")
                    priceTemp=price.strip()
                    priceTemp=priceTemp[1:]
                    
                    f.write(f"Laptop_price: {priceTemp}\n\n")
                    f.write(f"More_info: https://www.flipkart.com"+more+"\n\n")
                    
                    f.write('*'*600)
                    f.write('\n\n')    


                
            except Exception as e:
                     print(e)
        
        for laps in laptops:
            itemCost=''
            printtemp=0
           # y=FALSE
            company_name=laps.find('div', class_='_4rR01T').text
            specs=laps.find('div',class_='fMghEO').text
            price=laps.find('div',class_='_30jeq3 _1_WHN1').text
            more=str(laps.a['href'])
            co1=int(cost)+int(.1*int(cost))
            co2=int(cost)-int(.1*int(cost))
            priceTemp=price.strip()
            priceTemp=priceTemp[1:]
            strArray=priceTemp.split(",")
           
            for i in strArray:
                itemCost=itemCost+(i)
            
            printtemp=int(itemCost)
            #print(printtemp,'thodd')
            # for i in range(len(priceTemp)):
            #     if priceTemp[]==',':
            #         continue
            #     else:
            #         printtemp=printtemp*10+int(priceTemp(i))
            #print(printtemp,co2,co1)
        #if '3' in itemCost:# and  printtemp >co2:
           # print('yes')  
       
            if (printtemp>co2 and printtemp<co1) and processor.lower()  in specs.lower() and cmp.lower() in company_name.lower():
              
               

               print(f"Laptop_name: {company_name.strip()}\n\n")
                    
                    #specs=specs.replace('\ufffd'," ")
               print(f"Specs: {specs.strip()}\n\n")    
               print(f"Laptop_price: {priceTemp}\n\n")
               print(f"More_info: https://www.flipkart.com"+more+"\n\n")
        #print(f'file saved:{index}')
            
        print(' ')


if __name__ =='__main__':
    while True:
        find_laptops()
        print(f'waiting for 10 minutes....')
        time.sleep(600)
