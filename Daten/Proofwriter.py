import json
#import os

#folder_path = "E:\\BA\\Datenset\\proofwriter-dataset-V2020.12.3\\"
#for root, dirs, files in os.walk(folder_path):
    #for name in files:
        #file = os.path.join(root, name)
        #if file.endswith("train.jsonl"):
            #print("loading: ", file)
            #with open(file, encoding='utf-8') as f:
                #data = json.load(f)
            #del data
file = "E:\\BA\\Datenset\\proofwriter-dataset-V2020.12.3\\CWA\\meta-train.jsonl"
with open(file, 'r', encoding='utf-8') as f:
    data = json.load(f)
del data['maxD'], data['maxD'], data['NFact'], data['NRule'], data['triples'], data['rules'], data['maxD'], data['maxD']
with open(file, 'w', encoding='utf-8') as f:
    json.dump(data, f)