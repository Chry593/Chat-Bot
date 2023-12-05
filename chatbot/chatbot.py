# -*- coding: utf-8 -*-
"""
ChatBot

json dict[list[dict]]



"""
import json,time
from datetime import datetime
from difflib import get_close_matches


def load_memory_bot(path: str) -> dict:
    "carica il file json con tutte le domande e risposte del bot"
    with open(path,"r") as f:
        data = json.load(f)
    return data



def save_new_questions(data: str, path: str):
    "salva nel file json le nuove domande con le corrispettive risposte"
    with open (path,"w") as f:
        json.dump(data, f, indent=3)



def best_answer(user_quest:str ,lista_domande: list[str] ) -> str|None:
    "crea una lista con la risposta che si avvicina di più alla domanda"
    lista = get_close_matches(user_quest, lista_domande, n=1, cutoff=0.7) #70% 
    if lista:
        return lista[0]#primo elemento trovato
    return None



def answer(domanda: str, data: dict) -> str|None:
    "cerca la risposta"
    for d in data["domande"]:
        if d["domanda"] == domanda:
            return  d["risposta"]
    return None

def presentazione(testo: str):
    "stampa lettera per lettera con un ritardo di 5 millisecondi, pura estetica"
    for lettera in testo:
        print(lettera,end="",flush=True)
        time.sleep(0.03) 


def bot():
    
    #carico memoria
    memory = load_memory_bot("memory.json")
    
    #inizializzo bot
    testo = "Ciao sono Jarvis,un ChatBot, come posso aiutarti? Se vuoi uscire scrivi quit\n"
    presentazione(testo)
    while True:
        
        
        user_input = input("Tu: ")
        
        #uscita
        if user_input.lower() == "quit":
            break
        
        #creazione lista risposte
        lista_risposte = best_answer(user_input,[domanda["domanda"] for domanda in memory["domande"]])
        
        #se la lista contiene qualcosa
        if lista_risposte:
            risposta = answer(lista_risposte,memory)
            presentazione(f"\nJarvis: {risposta}\n")
            
        else: #nel caso non sa come rispondere gli andiamo a "dire" la risposta
            presentazione("\nJarvis: scusa ma non so la risposta, se me la dicessi ti potrei aiutarti in futuro\n")
            nuova_risposta = input("Scrivi la risposta o scrivi 'non ora': ")
            
            if nuova_risposta.lower() != "non ora":
                #aggiorniamo le domande/risposte
                memory["domande"].append({"domanda": user_input, "risposta" : nuova_risposta})
                #salviamo
                save_new_questions(memory, "memory.json")
                presentazione("\nJarvis: grazie! Ho imparato una nuova cosa\n")
                
            
        
        
        
        
        
            
        
if __name__ == "__main__":
    bot()          

        
        
        
        
        
        
        
        
        
        
