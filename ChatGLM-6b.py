# Ausgabe bei LLM - ChatGLM-6b
from transformers import AutoTokenizer, AutoModel
import time
import Kontexterstellung.anfrage_kontext as antext

a1 = time.time()
# Change to int4
tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b-int4", trust_remote_code=True)
model = AutoModel.from_pretrained("THUDM/chatglm-6b-int4", trust_remote_code=True).float()
model = model.eval()

text = antext.anfrage_kontext()
response, history = model.chat(tokenizer, text, history=[])
print('Antwort:')
print(response)

a2 = time.time()
print(f'the time cost: {a2 - a1} s')