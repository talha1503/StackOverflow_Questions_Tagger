import requests,os,csv,random
from bs4 import BeautifulSoup
import pandas as pd
#row_count = 2



base_url1 = "https://stackoverflow.com/questions/tagged/"
base_url2 = "?sort=MostVotes&tab=newest&page=1&pagesize=15"
count=0
tags = ['%20python','%20css','%20java','%20web-scraping','%20git','%20javascript','%20reactjs','%20node.js','%20jquery','%20php','%20flask']

#data = pd.read_csv('dataset.csv')

with open('dataset.csv','a',newline='') as file:
    wr = csv.writer(file,dialect='excel')
    while count<100001:
        max_labels = random.randint(1,10) 
        random_tags = [tags[random.randint(1,10)] for i in range(max_labels)]
        set_of_labels = set()
        for tag in random_tags:
            set_of_labels.add(tag)
        parameters = [x for x in random_tags]
        parameters = ''.join(parameters)
        final_url = base_url1 + parameters + base_url2
        page = requests.get(final_url)
        soup = BeautifulSoup(page.content,'html.parser')
        list_of_divs =soup.find_all('div',class_='question-summary')
        #print(len(list_of_divs))
        for i in range(len(list_of_divs)):
            row = ['0']*(len(tags)+1)
            text = list_of_divs[i].find_all('a',class_='question-hyperlink')
            ques = text[0].text
        #prepare an array  of ques , 1's and 0's for each question.Search for the element if it is present in the set , and then add 1 to 
        # the same position in the row array else , add 0 to the position . Next , add the row to the csv file and try or many iterations again and again. 
            row[0] = ques
            for tag in tags:
                if tag in set_of_labels:
                    row[tags.index(tag)+1] = '1'
                    #print(tag)
            wr.writerow(row)
        count += len(list_of_divs) 

