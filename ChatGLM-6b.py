from transformers import AutoTokenizer, AutoModel
import time

a1 = time.time()
# Change to int4
tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm-6b-int4", trust_remote_code=True)
model = AutoModel.from_pretrained("THUDM/chatglm-6b-int4", trust_remote_code=True).float()
model = model.eval()

response, history = model.chat(tokenizer, "extract keywords: Alice Washburn( 1860- 1929) was an American stage and film actress. She worked at the Edison, Vitagraph and Kalem studios. Her final film Snow White was her only known feature film. She died of heart attack in November 1929.", history=[])
print(response)

a2 = time.time()
print(f'the time cost: {a2 - a1} s')