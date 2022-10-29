import requests
from bs4 import *


def verificador(VERIF):
    concurso = 1

    JOGOS = []

    while concurso != 2534:
        
        response = requests.get(f"https://loteriascaixa-api.herokuapp.com/api/mega-sena/{concurso}", verify=False)
        dezenas = response.json()
        if dezenas["dezenas"]:
            JOGOS.append(dezenas["dezenas"])
        else:
            print(concurso)
            break
        concurso += 1


    l1 = VERIF
    for jogo in JOGOS:
        if jogo == l1:
            print("Jogo repetido: ")
            print(jogo)
            break

    print("FIM")