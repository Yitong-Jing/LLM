# Ausgabe bei LLM - Pythia-Chat-Base-7b
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import time
import Kontexterstellung.anfrage_kontext as antext

a1 = time.time()
# init
tokenizer = AutoTokenizer.from_pretrained("togethercomputer/Pythia-Chat-Base-7B-v0.16")
model = AutoModelForCausalLM.from_pretrained("togethercomputer/Pythia-Chat-Base-7B-v0.16", torch_dtype=torch.bfloat16)

# infer
text = antext.anfrage_kontext()
inputs = tokenizer(text, return_tensors='pt').to(model.device)
outputs = model.generate(**inputs, max_new_tokens=10, do_sample=True, temperature=0.8)
output_str = tokenizer.decode(outputs[0])
print('Antwort:')
print(output_str)

a2 = time.time()
print(f'the time: {a2 - a1} s')
