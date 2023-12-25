import pymysql
import keywords_llama_cpp as kyw

db = pymysql.connect(host='localhost',
                     user='root',
                     password='mysql',
                     database='inferenz_daten')

cursor = db.cursor()
#REGEXP
n = 0
keywords_result = kyw.keywords_output()
for i in keywords_result:
    sql = "SELECT context FROM WikiMultihopQA WHERE context REGEXP %s "
    cursor.execute(sql, i)
    results = cursor.fetchall()
    for row in results:
        n = n + 1
        context = row[0]
        print('第%s条', n)
        print("context=%s" % (context))
#try:
    # run SQL
    #cursor.execute(sql, params)
    # get the message
    #results = cursor.fetchall()
    #for row in results:
        #context = row[1]
        #print("context=%s" % (context))
#except:
    #print("Error: unable to fetch data")

# close database
db.close()