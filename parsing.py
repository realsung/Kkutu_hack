#-*-coding:utf-8-*-
import requests
from bs4 import BeautifulSoup
import re

get = requests.get('https://namu.wiki/w/%EB%81%84%ED%88%AC/%EA%B8%B4%20%EB%8B%A8%EC%96%B4/%ED%95%9C%EA%B5%AD%EC%96%B4')
source = get.text
soup = BeautifulSoup(source,'html.parser')
select_list = str(soup.find_all('div','wiki-paragraph'))
real_list = re.sub('<.*?>','',select_list)
real_list = re.sub('\d','',real_list)
real_list = re.sub('[.*]','',real_list)
real_list = re.sub(' ','',real_list)
real_list = re.sub('[a-z]','',real_list)
real_list = re.sub('[A-Z]','',real_list)
real_list = re.split('\W',real_list)
lst = [i for i in real_list if i]
lst = [i for i in lst if len(i) != 1]
print(lst)
"""
f = open('word','w')
for i in lst
	f.write(i)
	f.write('\n')
"""