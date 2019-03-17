    # -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class colors:
    def __init__(self):
        self.blue = "\033[94m"
        self.green = '\033[92m'
        self.red = '\033[91m'
        self.default = '\033[0m'
        self.purple = '\033[35m'
col = colors()
if __name__ == '__main__':
    print(col.purple+"""
                              _     _
                             ( \---/ )
                              ) . . (
________________________,--._(___Y___)_,--.________________________
                        `--'           `--'
        """+col.default)
    f = open('new_word',encoding='UTF-8')
    word_list = [] # 단어 가져올 배열
    for line in f:
        word_list.append(line.strip()) # 단어를 txt 파일에서 가져옴
    driver = webdriver.Chrome('/Users/realsung/Desktop/chromedriver') # 드라이버 경로
    URL = 'https://kkutu.co.kr' # 끄투 코리아 사이트
    driver.get(URL) # URL 연결
    table = [] # 이미 사용한 단어 check
    go = input(col.green+'go 입력하면 시작합니다 : ' + col.default)
    if(go == 'go'): # go라는 단어가 입력되면
        while True: # 무한 루프
            display_text = driver.find_element_by_class_name('jjo-display') # 화면에 보여지는 단어
            input_text = driver.find_element_by_xpath('//*[@id="game-input"]') # 입력 1
            real_input = driver.find_element_by_xpath("//input[contains(@id,'UserMessage')]") # 입력 2
            #get = driver.find_element_by_xpath('//*[@id="Middle"]/div[32]/div/div[1]/div[6]/div/div[1]') # text
            get = driver.find_element_by_xpath('//*[@id="Middle"]/div[33]/div/div[1]/div[6]/div/div[1]') # 
            #if(display_text.text == '게임 끝!'):
            #    raise NotImplementedError
            if(input_text.is_displayed()): # 입력 화면이 열리면
                target = get.text #화면에 보여지는 단어 가져옴
                time.sleep(0.3)
                if(len(target) == 4): # 두움법칙 특성상 4글자를 보여주는데 ()안에 있는 두음법칙 적용 단어를 가져옴
                    target = target[2] # 두움법칙 적용되는 단어를 target 변수에 담음
                print(col.blue+'받아 쳐야할 단어 : ' + col.default + target)
                for i in word_list: # 전체 단어에서 뽑을 것
                    if(i[0] == target[0]): # 첫 글자끼리 같으면
                        send_text = i # 그 단어를 보낼 단어 변수에 넣음
                        print(col.blue + '보낼 문장 : ' + col.default + send_text) 
                        del word_list[word_list.index(send_text)] # 보내는 단어 인덱스 제거
                        break # 탈출
                real_input.send_keys(send_text+Keys.RETURN) # 그 단어를 전송한다.
                time.sleep(0.3)
                if(display_text.text[0:5] == '이미 쓰인'): # 한방이거나 이미 쓰인 단어
                    del word_list[word_list.index(send_text)] # 인덱스 제거
                    print(col.red + '이미 쓰인 단어입니다' + col.default)
                elif(display_text.text[0:2] == '한방'):
                    del word_list[word_list.index(send_text)]
                    print(col.red + '한방 단어입니다' + col.default)
        time.sleep(0.4)