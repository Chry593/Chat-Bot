# Chat-Bot
ChatBot in grado di rispondere a domande fatte dall'utente e in grado di apprendere nuove risposte. 
È possibile usarlo in vari ambiti come quello dell'assistenza, dove gli si può far apprendere le 
risposte alle domande più gettonate fatte dai clienti così da poterli aiutare
Il programma è diviso in più funzioni:
  1) def load_memory_boat(path:str) -> carica la "memoria" del bot dove sono presenti le domande e le loro eventuali risposte
  2) def save_new_questions(data:str , path: str) -> salva le nuove domande-risposte nel file json
  3) def best_answer(user_quest: str, lista_domande: list[str]) -> crea una lista tramite la funzione *get_close_matches* con le risposte che si avvicinano di più alla domanda, e restituisce la prima risposta
  4) def answer(domanda: str, data: dict) -> cerca la domanda nel dizionario estratto dal file json
  5) def presentazione(testo: str) -> va a stampare le risposte del bot lettera per lettera,è una scelta stilistica
  6) def bot() -> la funzione principale, per prima cosa inizializzo la memoria del bot succesivamente chiedo all'user di fare la domanda, se user scrive "quit" si esce dal bot se no
     viene creata la lista di risposte più adeguate. Dopodichè si effettua un controllo per vedere se la lista contiene qualcosa ,se True allora cerchiamo la risposta tramite la funzione
     answer() e la mandiamo in output, se invece la lista è vuota allora il bot chiedere all'user di inserire lui la risposta così da memorizzare la risposta alla domanda fatta dall'user
     e dopodichè viene salvata nel file json.
