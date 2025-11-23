# Importa il decorator 'task' dalla libreria Invoke per creare task da CLI
from invoke import task


import os

# Definisce un task Invoke chiamato 'build'
@task
def build(c, docs=False):
    # Esegue 'poetry install' per installare tutte le dipendenze del progetto  
    c.run('poetry install')
    
    # Esegue il linter pycodestyle sulle cartelle contentscanner e tests
    # Verifica che il codice segua le convenzioni PEP 8
    c.run('poetry run pycodestyle contentscanner tests')
    
    # Esegue i test con pytest e misura la copertura del codice
    # 'coverage run -m pytest' esegue i test tracciando quali linee di codice sono state eseguite
    c.run('poetry run coverage run -m pytest contentscanner tests')
    
    # Crea il pacchetto distribuibile (wheel e tar.gz) usando Poetry 
    c.run('poetry build')
    
    # Verifica la presenza del file wordlist.txt
    if not os.path.exists('wordlist.txt'):
        print('No wordlist.txt found.')
    
    # Verifica l'esistenza della cartella dist/
    elif not os.path.exists('dist'):
        print('No dist/ found.')
    
    # Verifica che la cartella dist/ non sia vuota
    elif not os.listdir('dist'):
        print('No .whl or .gz found.')
    
    # Se tutti i check passano, procede con la build Docker
    else:
        # Rimuove un container Docker esistente chiamato 'contentscanner' (se esiste)
        c.run('docker rm -f contentscanner')
        
        # Builda l'immagine Docker dal Dockerfile nella directory corrente
        # Assegna il tag 'contentscanner_img' all'immagine
        c.run('docker build -t contentscanner_img .')
        
        # Crea un container Docker dall'immagine appena buildata
        # --name contentscanner: assegna il nome al container
        # -i -t: opzioni per l'interattività (interactive e TTY)
        c.run('docker container create -i -t --name contentscanner contentscanner_img')