import pymysql
import os
import json

def prem(db):
  cursor = db.cursor()
  cursor.execute("SELECT VERSION()")
  data = cursor.fetchone()
  print("Database version : %s " % data) # 结果表明已经连接成功
  cursor.execute("DROP TABLE IF EXISTS proofwriter_context") # 习惯性
  sql = """CREATE TABLE proofwriter_context (
       id CHAR(50) NOT NULL,
       context TEXT NOT NULL,
       PRIMARY KEY(id)
       )"""
  cursor.execute(sql) # 根据需要创建一个表格

def data_insert(db):
    folder_path = "E:\\BA\\Datenset\\proofwriter-dataset-V2020.12.3\\"
    for root, dirs, files in os.walk(folder_path):
        for name in files:
            file = os.path.join(root, name)
            if file.endswith("train.jsonl"):
                #n = n + 1
                print("loading: ", file)
                with open(file, encoding='utf-8') as f:
                    i = 0
                    while True:
                        i += 1
                        print(u'正在载入第%s行......' % i)
                        try:
                            lines = f.readline()  # 使用逐行读取的方法
                            text = json.loads(lines)  # 解析每一行数据
                            result = []
                            result.append((text['id'], text['theory']))  # 解析jsonl文件里的数据
                            print(result)

                            insert_re = "insert into proofwriter_context(id, context) values (%s, %s)"  # 插入到数据库中
                            cursor = db.cursor()
                            cursor.executemany(insert_re, result)
                            db.commit()  # 把修改的数据保存到数据库上

                        except Exception as e:
                            db.rollback()
                            print(str(e))
                            break

        #datenset_number = datenset_number + n
        #print("the number os Datenset in this folder:", n)
        #for name in dirs:
            #os.path.join(root, name)
    #print('the nuber of Datenset: ', datenset_number)




if __name__ == "__main__": # 起到一个初始化或者调用函数的作用
  db = pymysql.connect(host='localhost',
                       user='root',
                       password='mysql',
                       database='inferenz_daten')
  cursor = db.cursor()
  prem(db)
  data_insert(db)
  cursor.close()
