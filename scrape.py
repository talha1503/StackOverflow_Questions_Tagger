import requests,os,csv,random
from bs4 import BeautifulSoup
from pandas import read_csv

base_url1 = "https://stackoverflow.com/questions/tagged/"
base_url2 = "?sort=MostVotes&tab=newest&page=1&pagesize=15"
count=0
tags = ['%20python','%20css','%20java','%20web-scraping','%20git','%20javascript','%20reactjs','%20node.js','%20jquery','%20php','%20flask']


with open('dataset.csv','w') as csv_file:
    writer  = csv.writer(csv_file)
    while count<100001:
        max_labels = random.randint(1,11) 
        random_tags = [tags[radnom.randint(1,11)] for i in range(max_labels)]
        final_url = base_url1 + [x for x in random_tags] + base_url2
         

csv_file.close()


# df =  read_csv('dataset.csv',delim_whitespace = True)
# df.columns = tags
# df.to_csv('dataset_1.csv')