import urllib.request
from bs4 import BeautifulSoup
import sys

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
        question= soup.find_all('div', {'class': 'question fmt'})
        #question为获取到问题的题目
        for i in question:
            content = i.find_all('p')
            print("问题内容是         :         "+content[0].string)
        #获取到问题的数量
        answerCount = soup.find('h2',{'id':'answers-title'})
        print(answerCount.text)
        answers = [answerCount]
        #获取到包含所有回答的Set
        answerall = soup.find_all('div',{'class':'answer fmt'})
        for anscount,answer in enumerate(answerall):
            #加入到answer的集合众
           if answer not in answers:
               print("这是第  %s"%anscount+"   条答案")
               answers.append(answerall)
               #获取到所有的p标签的内容
               answercontent = answer.find_all('p')
               for i,con in enumerate(answercontent):
                    print(con.text)

    if __name__ == '__main__':
         soup = geturl("https://segmentfault.com/q/1010000000170658")
         getcontent(soup)