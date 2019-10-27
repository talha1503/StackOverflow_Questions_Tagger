import requests,os,csv,random
from bs4 import BeautifulSoup
import pandas as pd



base_url1 = "https://stackoverflow.com/questions/tagged/"
base_url2 = "?sort=MostVotes&tab=newest&page=1&pagesize=15"
count=0
tags = ['%20python','%20css','%20java','%20web-scraping','%20git','%20javascript','%20reactjs','%20node.js','%20jquery','%20php','%20flask']


with open('dataset.csv','a',newline='') as file:
    wr = csv.writer(file,dialect='excel')
    while count<100001:
        max_labels = random.randint(1,10) 
        random_tags = [tags[random.randint(1,10)] for i in range(max_labels)]
        set_of_labels = set()
        parameters = [x for x in random_tags]
        parameters = ''.join(parameters)
        final_url = base_url1 + parameters + base_url2
        page = requests.get(final_url)
        soup = BeautifulSoup(page.content,'html.parser')
        list_of_divs =soup.find_all('div',class_='question-summary')
        for i in range(len(list_of_divs)):
            row = ['0']*(len(tags)+1)
            text = list_of_divs[i].find_all('a',class_='question-hyperlink')
            ques = text[0].text
            row[0] = ques
            for tag in tags:
                if tag in set(random_tags):
                    row[tags.index(tag)+1] = '1'
            wr.writerow(row)
        count += len(list_of_divs) 

