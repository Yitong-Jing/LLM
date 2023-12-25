import json
import numpy as np



with open("E:\\BA\\Datenset\\2WikiMultihopQA\\dev.json", encoding='utf-8') as f:

    lines = f.readline()  # 使用逐行读取的方法
    text = json.loads(lines)  # 解析每一行数据

    for i in text:
        #id = i['_id']
        daten = []
        result = []
        for j in range(len(i['context'])):
            result.extend(i['context'][j][1])
        #context = ' '.join(result)
        daten.append((i['_id'], ' '.join(result)))
        print(daten)
f.close()