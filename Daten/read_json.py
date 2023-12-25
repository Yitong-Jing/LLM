# read die Daten in verschiedene json Datai

import os


folder_path = "E:\\BA\\Datenset\\proofwriter-dataset-V2020.12.3\\"
x = 0
for root, dirs, files in os.walk(folder_path):
    n = 0
    for name in files:
        file = os.path.join(root, name)
        if file.endswith("train.jsonl") or file.endswith("dev.jsonl"):
            n = n + 1
            print(file)
            """
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
                    except Exception as e:
                        print()
                        break
            """
    print("the number os Datenset in this folder:", n)
    x = x + n
    #for name in dirs:
        #os.path.join(root, name)

print('the nuber of Datenset: ', x)

