import pymysql


class GetMysqlDb:


    def InsertQuestion(db,questionid,question,answercount):
        try:
          conn = pymysql.connect(host='127.0.0.1', port=3306, user="root", passwd="616675", db='py',charset='utf8')
        except:
            print("mysql连接过程出现错误，请检查")
        cur = conn.cursor()
        sql = "insert into %s(questionid,question,answercount) VALUES( %s,'%s','%s');"%(db,questionid,question,answercount)
        print(sql)
        try:
         cur.execute(sql)
        except:
            print("执行sql出现问题，请检查")
        conn.commit()
        cur.close()
        conn.close()

    def InserAnswer(db,answerid,answercontent):
        try:
            conn = pymysql.connect(host='127.0.0.1', port=3306, user="root", passwd="616675", db='py', charset='utf8')
        except:
            print("mysql连接过程出现错误，请检查")
        cur = conn.cursor()
        sql = "insert into %s(answerid,answercontent) VALUES( %s,'%s');" % (db, answerid,answercontent)
        try:
            cur.execute(sql)
        except:
            print("执行sql出现问题，请检查")
        conn.commit()
        cur.close()
        conn.close()