# Kontext mit or und and in Dantenbank suche
import pymysql
import Kontexterstellung.keywords as kyw
import random

#Kontext mit AND suche
def select_context_AND(db, anfrage):
    cursor = db.cursor()
    keywords = kyw.keywords_output(anfrage)
    context = ''
    if (len(keywords) == 0):
        return context
    else:
        sql = "SELECT context FROM WikiMultihopQA WHERE context REGEXP %s "
        cursor.execute(sql, keywords[0])
        db_results = cursor.fetchall()

        if len(db_results) == 0:
            print('Keine Info über diese Anfrage in Datenbank')
            return context
        else:
            matched_contexts = []
            for context_tuple in db_results:
                context_str = str(context_tuple)
                i = 1
                while keywords[i] in context_str:
                    i += 1
                    if i == len(keywords):
                        matched_contexts.append(context_str)
                        print('Gefundte Kontexte:', context_str)
                        break
            context = ' '.join(matched_contexts)
            print('gefundte Info in Datenbank:', context)
            return context


#Kontext mit OR suche
def select_context_OR(db, anfrage):
    cursor = db.cursor()
    keywords = kyw.keywords_output(anfrage)
    context = ''
    if (len(keywords) == 0):
        return context
    else:
        db_results = ()
        matched_contexts = []
        for keyword in keywords:
            sql = "SELECT context FROM proofwriter_context WHERE context REGEXP %s "
            #try:
            cursor.execute(sql, keyword)
            db_result = cursor.fetchall()
            db_results += db_result

        if len(db_results) >= 3:
            random_db_results = random.sample(db_results, 3)
            context_str = str(random_db_results)
            matched_contexts.append(context_str)
            context = ' '.join(matched_contexts)
            print('gefundte Info in Datenbank:', context)
            return context

        elif 3 >= len(db_results) > 0:
            context_str = str(db_results)
            matched_contexts.append(context_str)
            context = ' '.join(matched_contexts)

        else:
            print('Keine Info über diese Anfrage in Datenbank')
            #except:
                #print("Error: unable to fetch data")
        return context

def db_info(anfrage):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='mysql',
                         database='inferenz_daten')
    cursor = db.cursor()
    p = input('Wenn Sie genauere Informationen möchten, geben Sie 0 ein. Wenn Sie eine allgemeinere Antwort wünschen, geben Sie 1 ein. ')
    p = int(p)
    if p == 0:
        info = select_context_AND(db, anfrage)
    elif p == 1:
        info = select_context_OR(db, anfrage)
    cursor.close()
    return info

#db_info('Do both films The Falcon (Film) and Valentin The Good have the same director?')