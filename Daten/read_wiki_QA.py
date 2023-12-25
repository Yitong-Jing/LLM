# read die Daten _id and setences in 2WikiMultihopQA
import pymysql
import os
import json

def prem(db):
  cursor = db.cursor()
  cursor.execute("SELECT VERSION()")
  data = cursor.fetchone()
  print("Database version : %s " % data) # Überprüfen, ob die Verbindung erfolgreich hergestellt wurde.
  cursor.execute("DROP TABLE IF EXISTS Wiki_QA")  # 习惯性
  sql = """CREATE TABLE Wiki_QA (
       id CHAR(50) NOT NULL,
       question TEXT NOT NULL,
       answer TEXT NOT NULL,
       PRIMARY KEY(id),
       FOREIGN KEY(id) REFERENCES Wiki_context(id)
       )"""
  cursor.execute(sql)

def data_insert(db):
    folder_path = "E:\\BA\\Datenset\\2WikiMultihopQA\\"
    for name in os.listdir(folder_path):
        file = os.path.join(folder_path, name)
        if file.endswith('.json'):
            print(file)
            with open(file, encoding='utf-8') as f:
                n = 0
                while True:
                    try:
                        lines = f.readline()  # 使用逐行读取的方法
                        text = json.loads(lines)  # 解析每一行数据
                        for i in text:
                            n += 1
                            print(u'正在载入第%s行......' % n)
                            id = i['_id']
                            question = i['question']
                            answer = i['answer']
                            daten = []
                            daten.append((id, question, answer))
                            print(daten)
                            insert_re = "insert into Wiki_QA(id, question, answer) values (%s, %s, %s)"  # 插入到数据库中
                            cursor = db.cursor()
                            cursor.executemany(insert_re, daten)
                            db.commit()  # 把修改的数据保存到数据库上
                    except Exception as e:
                        db.rollback()
                        print(str(e))
                        break


if __name__ == "__main__": # 起到一个初始化或者调用函数的作用
  db = pymysql.connect(host='localhost',
                       user='root',
                       password='mysql',
                       database='inferenz_daten')
  cursor = db.cursor()
  prem(db)
  data_insert(db)
  cursor.close()