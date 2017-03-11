import urllib.request
from bs4 import BeautifulSoup
import sys
import re
import pymysql
from MysqlConn import GetMysqlDb

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
            questionContent = content[0].string
        #获取到问题的数量
        answerCount = soup.find('h2',{'id':'answers-title'})
        pattern = re.compile('\d+')
        answerCountRe = pattern.findall(answerCount.text)
        #获取到包含所有回答的Set
        answerall = soup.find_all('div',{'class':'answer fmt'})
        list.append(questionContent)
        list.append(answerCountRe[0])
        list.append(answerall)
        return list
    def connectmysql(urlid,question,answercount):
        print("s")


    if __name__ == '__main__':
         soup = geturl("https://segmentfault.com/q/1010000000170658")
         url = r"https://segmentfault.com/q/1010000000170658"
         patten = r"\d\d*"
         parrern = re.compile(patten)
         urlid = parrern.findall(url)
         print("问题的id是"+urlid[0])
         list = getcontent(soup)
         question = list[0]
         print("问题的题目是"+question)
         answercount = list[1]
         print("答案的数量是  "+answercount)
         GetMysqlDb.InsertQuestion('py.question', urlid[0], question, answercount)
         listOfAnswer = list[2]
         for i,answer in enumerate(listOfAnswer):
             answerid = urlid[0]+str(i)
             GetMysqlDb.InserAnswer('py.answer',answerid,answer.text)
