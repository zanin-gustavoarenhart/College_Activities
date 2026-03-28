import os, time

def cleanScreen():
    os.system("cls")

def timeWait(seconds):
    time.sleep(seconds)

def writeScreen(text):
    print(text)

def logQueue():
    try:
        file = open("Log Atendimento.txt", "a")
        file.write(f"\nÚltima Senha Chamada: {queue_called.__len__()}\nÚltimas Senhas Chamadas: {queue_last_tickets}\nTotal de Senhas: {last_ticket}\nSenhas Não Chamadas: {queue_ticket}\nSenhas Chamadas:{queue_called}\n")
        file.close()
    except:
        file = open("Log Atendimento.txt", "w")
        file.write(f"Última Senha Chamada: {queue_called.__len__()}\nÚltimas Senhas Chamadas: {queue_last_tickets}\nTotal de Senhas: {last_ticket}\nSenhas Não Chamadas: {queue_ticket}\nSenhas Chamadas:{queue_called}\n")
        file.close()

class Queue:
    def __init__(self):
        self._vet = []
    
    def enqueue(self, item):
        self._vet.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self._vet.pop(0)

    def front(self):
        return self._vet[0]
                
    def is_empty(self):
        if len(self._vet) == 0:
            return True
        return False
        
    def __len__(self):
        return len(self._vet)

    def __str__(self):
        return str(self._vet)

last_ticket = 0
queue_called = Queue()
queue_ticket = Queue()
queue_last_tickets = Queue()
