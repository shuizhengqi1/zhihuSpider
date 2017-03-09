import urllib.request
from bs4 import BeautifulSoup
import sys
import re
import pymysql

class SingelePageSpider:
    def __init__(self):
        self.page = 1
        self.pages = []
        self.enabled = False

    def geturl(url):
        Url = url
        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        headers = {'User-Agent': user_agent}
        Req = urllib.request.Request(url,headers=headers)
        res = urllib.request.urlopen(Req)
        soup = BeautifulSoup(res,"html.parser")
        return soup

    def getcontent(soup):
        list = []

        question= soup.find_all('div', {'class': 'question fmt'})
        #question为获取到问题的题目
        for i in question:
            content = i.find_all('p')
            print("问题内容是         :         "+content[0].string)
            questionContent = content[0].string
        #获取到问题的数量
        answerCount = soup.find('h2',{'id':'answers-title'})
        print(answerCount.text)
        answers = [answerCount]
        #获取到包含所有回答的Set
        answerall = soup.find_all('div',{'class':'answer fmt'})
        list.append(questionContent)
        list.append(answerall)
        return list
    def connectmysql(urlid,list):
        conn = pymysql.connect(host='127.0.0.1',port=3306,user="root",passwd="616675",db='py')
        cur = conn.cursor()
        question = list[0]

        sql="insert into answer(AnsId,Question,AnswerContent) VALUES("+urlid+","+question+","+")"
        print(sql)
        cur.execute(sql)
        rows = cur.fetchall()
        print(rows)

    if __name__ == '__main__':
         soup = geturl("https://segmentfault.com/q/1010000000170658")
         url = r"https://segmentfault.com/q/1010000000170658"
         patten = r"\d\d*"
         parrern = re.compile(patten)
         urlid = parrern.findall(url)
         print(urlid[0])
         list = getcontent(soup)
         print(len(list))
         connectmysql(urlid,list)