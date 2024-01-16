from llama_cpp_ import Llama
import Kontext_OR_AND as kt

#Antwort mit Llms generieren
def generate_text(model, message):
    prompt = f"[INST] {message.strip()} [/INST]"
    output = model(prompt)
    answer = output["choices"][0]["text"]
    return answer

#Kontext mit Anfrage des Nutzers und Dantenbankinformationen
def Antwort():
    model = Llama(model_path="C:/Users/11609/.conda/envs/llama2_jing/Lib/site-packages/pip/_internal/models/Lamada/7B/llama-2-7b-chat.Q4_0.gguf")
    anfrage = input('Bitte schreiben Sie die Anfrage: ')
    info = kt.db_info(anfrage) #str
    kontext = anfrage + info #str
    print('erstellte Kontext: ')
    print(kontext)
    print('Antwort:')
    antwort = generate_text(model, kontext)
    print(antwort)
    return antwort

#Antwort()
