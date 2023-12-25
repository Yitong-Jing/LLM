from llama_cpp import Llama
import time

a1 = time.time()
def generate_text(model,message):
    prompt = f"[INST] {message.strip()} [/INST]"
    output = model(prompt)
    answer = output["choices"][0]["text"]
    return answer

if __name__ == '__main__':
    model = Llama(model_path = "D:/LLM_Modelle/vicuna_13b/vicuna-13b-v1.5.Q2_K.gguf")
    print("who are you")
    #print(dir(model))
    print(generate_text(model, "What is water?"))
    print("")
a2 = time.time()
print(f'the time: {a2 - a1} s')