import requests
from bs4 import BeautifulSoup
import pprint
import re

    
res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text,'html.parser')
soup2 = BeautifulSoup(res2.text,'html.parser')
links = soup.select('.storylink')
links2 = soup.select('.storylink')
votes = soup.select('.score')
votes2 = soup.select('.score')
mega_links = links + links2
mega_votes = votes + votes2

def get_votes(votes):
    votesPattern = re.compile(r'\d+')
    votes = int("".join(votesPattern.findall(votes)))
    return votes
  
def create_custom_hn(links,votes):
    hn = []
    for idx,item in enumerate(links):
        title = item.getText()
        href = item.get("href",None)
        points = get_votes(votes[idx].get_text())
        if(points > 100):
            hn.append(({'title':title,'link':href,'votes':points}))
            for item in hn:
                hn.sort(key=lambda x:x['votes'],reverse=True)
    return hn

pprint.pprint(create_custom_hn(mega_links,mega_votes))











