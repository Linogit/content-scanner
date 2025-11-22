# Progetto Automated Software Delivery

## Descrizione:

Questo progetto consiste in un processo di build completo utilizzando Python, Poetry, Invoke e Docker. L'obiettivo e' automatizzare l'intero ciclo di vita del software,
dalla gestione delle dipendenze alla creazione di immagini Docker pronte per la produzione.

## Prerequisiti:
- Python 3.8+
- invoke
- poetry
- docker

## Utilizzo:
Ricorda di mettere nella root del progetto il file wordlist.txt

L'istruzione ```inv build``` avviera' il processo di build:
1. Installazione delle dipendenze
2. Verifica dello stile del codice PEP 8
3. Esecuzione dei casi di test
4. Creazione dei .whl e .tar.gz
5. Creazione dell'immagine e del container di docker