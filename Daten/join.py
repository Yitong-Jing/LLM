import pymysql

db = pymysql.connect(host='localhost',
                     user='root',
                     password='mysql',
                     database='inferenz_daten')

cursor = db.cursor()

sql = "SELECT theory.id, theory.theory, QA.question, QA.answer FROM theory, QA WHERE theory.id = 'RelNoneg-OWA-D0-3702'"
try:
    # run SQL
    cursor.execute(sql)
    # get the message
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        theory = row[1]
        question = row[2]
        answer = row[3]
        print("id=%s,theory=%s,question=%s,answer=%s" % \
              (id, theory, question, answer))
except:
    print("Error: unable to fetch data")

# close database
db.close()