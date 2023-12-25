from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import time

a1 = time.time()
# init
tokenizer = AutoTokenizer.from_pretrained("D:/LLM_Modelle/OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5")
model = AutoModelForCausalLM.from_pretrained("D:/LLM_Modelle/OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5", torch_dtype=torch.bfloat16)

# infer
inputs = tokenizer("<human>: What is water?\n<bot>:", return_tensors='pt').to(model.device)
outputs = model.generate(**inputs, max_new_tokens=10, do_sample=True, temperature=0.8)
output_str = tokenizer.decode(outputs[0])
print(output_str)

a2 = time.time()
print(f'the time: {a2 - a1} s')
