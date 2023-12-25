from llama_cpp import Llama

def generate_text(model,message):
    prompt = f"[INST] {message.strip()} [/INST]"
    output = model(prompt)
    answer = output["choices"][0]["text"]
    return answer

if __name__ == '__main__':
    model = Llama(model_path = "C:/Users/11609/.conda/envs/llama2_jing/Lib/site-packages/pip/_internal/models/Lamada/7B/llama-2-7b-chat.Q4_0.gguf")
    print('what is water')
    text = generate_text(model, 'what is water')
    print(text)