import os
import re
import requests
from datetime import datetime as dt
import dotenv
from shared_library.shared_library import generate_workfolder, delete_workfolder
from listener.listener import Listener
from speaker.speaker import Speaker

dotenv.load_dotenv()

ACTIVATION_WORD = os.environ.get("ACTIVATION_WORD")

print("ACTIVATION WORD:", ACTIVATION_WORD)

if __name__ == "__main__":
    workfolder = generate_workfolder()
    speaker = Speaker(workfolder.name)
    listener = Listener()

    while True:
        try:
            content = str(listener.listen()).lower()
            print('>', content)
            if content.startswith(ACTIVATION_WORD):
                print("como posso ajudar?")
                speaker.play_audio(speaker.create_audio("como posso ajudar?"))
                command = str(listener.listen()).lower()
                print('>', command)
                if command == "que horas são":
                    time = dt.now()
                    s_hour = 's' if time.hour != 1 else ''
                    s_minute = 's' if time.minute != 1 else ''
                    time_str = f"são {time.hour} hora{s_hour} e {time.minute} minuto{s_minute}"
                    print(time_str)
                    speaker.play_audio(speaker.create_audio(time_str))
                elif re.match("(.* )?temperatura (em|no|na) .*", command):
                    cidade = command[command.index("temperatura") + 15:]
                    # r = requests.get(f"https://goweather.herokuapp.com/weather/{cidade}")
                    r = requests.get(f"https://wttr.in/{cidade}?format=\"%t\"")
                    if r.status_code != 200:
                        print("não sei a temperatura para essa cidade")
                        speaker.play_audio(speaker.create_audio("não sei a temperatura para essa cidade"))
                    else:
                        # temperatura = r.json()["temperature"][:3].replace("+", "")
                        temperatura = r.text.replace("+", "")
                        prep = command[command.index("temperatura") + 12:command.index("temperatura") + 14]
                        response_text = f"Está fazendo {temperatura} {prep} {cidade}"
                        print(response_text)
                        speaker.play_audio(speaker.create_audio(response_text))
                elif re.match("qual (o valor|a cotação) do (dolar|euro|dólar) em reais", command):
                    moeda = command[command.index("do") + 3:command.index("em reais")-1]
                    # print(moeda)
                    if moeda == "dólar" or moeda == "dolar":
                        moeda_symbol = "usd"
                    elif moeda == "euro":
                        moeda_symbol = "eur"
                    else:
                        raise ZeroDivisionError()
                    r = requests.get(f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/brl/{moeda_symbol}.json")
                    if r.status_code != 200:
                        raise ZeroDivisionError()
                    else:
                        conv = round(1/r.json()[moeda_symbol],2)
                        response_text = f"O valor do {moeda} é de {conv} reais"
                        print(response_text)
                        speaker.play_audio(speaker.create_audio(response_text))
                elif re.match("quanto(s)? são (\$)?(\d+) (dolar|euro|dólar)(s|es)? em reais", command):
                    valores = command[command.index("são") + 4:command.index("em reais")-1].split(" ")
                    # print(valores)
                    if valores[1].startswith("dólar") or valores[1].startswith("dolar"):
                        moeda_symbol = "usd"
                    elif valores[1].startswith("euro"):
                        moeda_symbol = "eur"
                    else:
                        raise ZeroDivisionError()
                    r = requests.get(f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/brl/{moeda_symbol}.json")
                    if r.status_code != 200:
                        raise ZeroDivisionError()
                    else:
                        conv = round(1/r.json()[moeda_symbol],2)
                        result = int(valores[0])*conv
                        response_text = f"{valores[0]} {valores[1]} são {result} reais"
                        print(response_text)
                        speaker.play_audio(speaker.create_audio(response_text))
                else:
                    print("não consigo te ajudar com isso")
                    speaker.play_audio(speaker.create_audio("não consigo te ajudar com isso"))
        except ZeroDivisionError:
            print("não consigo te ajudar com isso")
            speaker.play_audio(speaker.create_audio("não consigo te ajudar com isso"))
            continue
        except KeyboardInterrupt: break
        # except:
        #     print("não consigo te ajudar com isso")
        #     speaker.play_audio(speaker.create_audio("não consigo te ajudar com isso"))
        #     continue
    delete_workfolder(workfolder)
