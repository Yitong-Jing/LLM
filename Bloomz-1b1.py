# Ausgabe bei LLM - Bloomz-1b1
from transformers import AutoModelForCausalLM, AutoTokenizer
import time
import Kontexterstellung.anfrage_kontext as antext

a1 = time.time()
checkpoint = "bigscience/bloomz-1b1"

tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForCausalLM.from_pretrained(checkpoint)

text = antext.anfrage_kontext()
inputs = tokenizer.encode(text, return_tensors="pt") #prompt
outputs = model.generate(inputs, min_length=50, max_new_tokens=100, do_sample=True)
print('Antwort:')
print(tokenizer.decode(outputs[0])) #Verwenden den Tokenizer, um die generierten Ergebnisse zu dekodieren

a2 = time.time()
print(f'time cost is {a2 - a1} s')
