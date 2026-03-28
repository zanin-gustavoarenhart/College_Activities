from linePanel_assets import cleanScreen, timeWait, writeScreen, logQueue
from linePanel_assets import last_ticket, queue_called, queue_ticket, queue_last_tickets

cleanScreen()

while True:
    writeScreen(f"Última Senha Chamada: {queue_called.__len__()}")
    writeScreen(f"Últimas Senhas Chamadas: {queue_last_tickets}")
    writeScreen(f"Total de Senhas: {last_ticket}")

    option = str(input("\nSelecione uma Opção:\n0 - Sair\n1 - Obter nova senha\n2 - Chamar próxima senha\nOpção: "))
    if option == "1":
        cleanScreen()
        last_ticket += 1
        queue_ticket.enqueue(last_ticket)
    
    elif option == "2":
        cleanScreen()
        if queue_ticket.is_empty() is False:
            queue_called.enqueue(queue_ticket.front())

            if queue_called.is_empty() is False and queue_last_tickets.__len__() <= 4:
                queue_last_tickets.enqueue(queue_ticket.front())

            elif queue_called.is_empty() is False and queue_last_tickets.__len__() == 5:
                queue_last_tickets.dequeue()
                queue_last_tickets.enqueue(queue_ticket.front())

            queue_ticket.dequeue()

        else:
            writeScreen("Não há senhas em espera!\n")
            timeWait(0.75)
            cleanScreen()

    elif option == "0":
        logQueue()
        break

    else:
        cleanScreen()
