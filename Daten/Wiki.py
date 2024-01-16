# read die Daten _id and setences in 2WikiMultihopQA
import pymysql
import json

def prem(db):
  cursor = db.cursor()
  cursor.execute("SELECT VERSION()")
  data = cursor.fetchone()
  print("Database version : %s " % data) # Überprüfen, ob die Verbindung erfolgreich hergestellt wurde.
  cursor.execute("DROP TABLE IF EXISTS WikiMultihopQA")  # 习惯性
  sql = """CREATE TABLE WikiMultihopQA (
       id CHAR(50) NOT NULL,
       id_context CHAR(50) NOT NULL,
       context TEXT NOT NULL,
       PRIMARY KEY(id_context)
       )"""
  cursor.execute(sql)

def data_insert(db):
    with open("E:\\BA\\Datenset\\2WikiMultihopQA\\train.json", encoding='utf-8') as f:
        n = 0
        while True:
            try:
                lines = f.readline()  # 使用逐行读取的方法
                text = json.loads(lines)  # 解析每一行数据
                for i in text:
                    n += 1
                    print(u'正在载入第%s行......' % n)
                    for j in range(len(i['context'])):
                        setence = ' '.join(i['context'][j][1]) #str
                        result = []
                        result.append((i['_id'], i["_id"] + str(j), setence))  # 解析jsonl文件里的数据
                        print(result)
                        insert_re = "insert into WikiMultihopQA(id, id_context, context) values (%s, %s, %s)"  # 插入到数据库中
                        cursor = db.cursor()
                        cursor.executemany(insert_re, result)
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