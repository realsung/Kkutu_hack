import requests
from bs4 import BeautifulSoup
import re
web = requests.get('https://kkukowiki.kr/wiki/%EB%81%84%ED%88%AC%EC%BD%94%EB%A6%AC%EC%95%84/%EA%B8%B4_%EB%8B%A8%EC%96%B4/%ED%95%9C%EA%B5%AD%EC%96%B4/%E3%85%8E')
source = web.text
soup = BeautifulSoup(source,'html.parser')
select_list = str(soup.find_all('a'))
real_list = re.sub('<.*?>','',select_list)
real_list = re.sub('\d','',real_list)
real_list = re.sub('[.*]','',real_list)
real_list = re.sub(' ','',real_list)
real_list = re.sub('[a-z]','',real_list)
real_list = re.sub('[A-Z]','',real_list)
real_list = re.split('\W',real_list)
lst = [i for i in real_list if i]
good = [i for i in lst if len(i) != 1]
print(good)
f = open('killword','w')
for i in good:
	f.write(i)
	f.write('\n')