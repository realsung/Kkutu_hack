#-*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

"""
change_table = {
    '롭' : '놉',
    '뉵' : '육',
    '릭' : '익',
    '력' : '역',
    '랄' : '날',
    '랏' : '낫',
    '림' : '임',
    '률' : '율',
    '랴' : '야',
    '녁' : '역',
    '릿' : '잇',
    '룰' : '눌',
    '례' : '예',
    '릇' : '늣',
    '렁' : '넝',
    '뢰' : '뇌',
    '롄' : '옌',
    '뇽' : '용',
    '륵' : '늑',
    '륨' : '윰'
    '류' : '유'
}
"""

if __name__ == '__main__':
    #global display_text
    #global real_text
    f = open('new_word')
    word_list = []
    for line in f:
    	word_list.append(line.strip())
    real_text = "기본값"
    driver = webdriver.Chrome('./chromedriver')
    URL = 'https://kkutu.co.kr'
    driver.get(URL)

    table = [] # 이미 사용한 단어 check

    go = input('시작하려면 go를 입력하세요 : ')
    if(go == 'go'):	
        while True:
            display_text = driver.find_element_by_class_name('jjo-display')
            input_text = driver.find_element_by_xpath('//*[@id="game-input"]')
            real_input = driver.find_element_by_xpath("//input[contains(@id,'UserMessage')]") #input
            #//ITEM/*[starts-with(text(),'2552')]/following-sibling::*
            #get = driver.find_element_by_xpath('//*[@id="Middle"]/div[32]/div/div[1]/div[6]/div/div[1]') # text
            get = driver.find_element_by_xpath('//*[@id="Middle"]/div[33]/div/div[1]/div[6]/div/div[1]')
            target = get.text #첫글자
            #word_list.remove(send_text)
            #if(display_text.text == '게임 끝!'):
            #    raise NotImplementedError
            if(input_text.is_displayed()):
                if(target[0] == '릿'):
                    target[0] == '잇'
                elif(target[0] == '릇'):
                    target[0] == '늣'
                print("받아쳐야하는 글자 : " + target)
                time.sleep(0.3)
                for i in word_list:
                    if(i[0] == target[0]):
                        send_text = i
                        print('보낼 단어 : ' + send_text)
                        del word_list[word_list.index(send_text)]
                        break
                real_input.send_keys(send_text+Keys.RETURN)
                time.sleep(0.3)
                if(display_text.text[0:5] == '이미 쓰인' or display_text.text[0:2] == '한방'):
                    del word_list[word_list.index(send_text)]
        time.sleep(0.4)
