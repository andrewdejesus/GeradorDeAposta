from logging import exception
import requests
from bs4 import *


def verificador1(VERIF):
    concurso = 1

    JOGOS = []

    while True:
        try:
            if concurso == 200:
                break
            else:
                response = requests.get(f"https://loteriascaixa-api.herokuapp.com/api/mega-sena/{concurso}", verify=False)
                dezenas = response.json()
                if dezenas["dezenas"]:
                    JOGOS.append(dezenas["dezenas"])
                else:
                    print(concurso)
                    break
                concurso += 1
        except:
            break

    try:
        l1 = VERIF
        for jogo in JOGOS:
            if jogo == l1:
                print("Jogo repetido: ")
                print(jogo)
                break
    except:
        print("Algo deu errado")
        pass

    

def verificador2(VERIF):
    concurso = 200

    JOGOS = []

    while True:
        try:
            if concurso == 400:
                break
            else:
                response = requests.get(f"https://loteriascaixa-api.herokuapp.com/api/mega-sena/{concurso}", verify=False)
                dezenas = response.json()
                if dezenas["dezenas"]:
                    JOGOS.append(dezenas["dezenas"])
                else:
                    print(concurso)
                    break
                concurso += 1
        except:
            break

    try:
        l1 = VERIF
        for jogo in JOGOS:
            if jogo == l1:
                print("Jogo repetido: ")
                print(jogo)
                break
    except:
        print("Algo deu errado")
        pass

def verificador3(VERIF):
    concurso = 400

    JOGOS = []

    while True:
        try:
            if concurso == 600:
                break
            else:
                response = requests.get(f"https://loteriascaixa-api.herokuapp.com/api/mega-sena/{concurso}", verify=False)
                dezenas = response.json()
                if dezenas["dezenas"]:
                    JOGOS.append(dezenas["dezenas"])
                else:
                    print(concurso)
                    break
                concurso += 1
        except:
            break

    try:
        l1 = VERIF
        for jogo in JOGOS:
            if jogo == l1:
                print("Jogo repetido: ")
                print(jogo)
                break
    except:
        print("Algo deu errado")
        pass

def verificador4(VERIF):
    concurso = 600

    JOGOS = []

    while True:
        try:
            if concurso == 800:
                break
            else:
                response = requests.get(f"https://loteriascaixa-api.herokuapp.com/api/mega-sena/{concurso}", verify=False)
                dezenas = response.json()
                if dezenas["dezenas"]:
                    JOGOS.append(dezenas["dezenas"])
                else:
                    print(concurso)
                    break
                concurso += 1
        except:
            break

    try:
        l1 = VERIF
        for jogo in JOGOS:
            if jogo == l1:
                print("Jogo repetido: ")
                print(jogo)
                break
    except:
        print("Algo deu errado")
        pass

def verificador5(VERIF):
    concurso = 800

    JOGOS = []

    while True:
        try:
            if concurso == 1000:
                break
            else:
                response = requests.get(f"https://loteriascaixa-api.herokuapp.com/api/mega-sena/{concurso}", verify=False)
                dezenas = response.json()
                if dezenas["dezenas"]:
                    JOGOS.append(dezenas["dezenas"])
                else:
                    print(concurso)
                    break
                concurso += 1
        except:
            break

    try:
        l1 = VERIF
        for jogo in JOGOS:
            if jogo == l1:
                print("Jogo repetido: ")
                print(jogo)
                break
    except:
        print("Algo deu errado")
        pass

def verificador6(VERIF):
    concurso = 1000

    JOGOS = []

    while True:
        try:
            if concurso == 1200:
                break
            else:
                response = requests.get(f"https://loteriascaixa-api.herokuapp.com/api/mega-sena/{concurso}", verify=False)
                dezenas = response.json()
                if dezenas["dezenas"]:
                    JOGOS.append(dezenas["dezenas"])
                else:
                    print(concurso)
                    break
                concurso += 1
        except:
            break

    try:
        l1 = VERIF
        for jogo in JOGOS:
            if jogo == l1:
                print("Jogo repetido: ")
                print(jogo)
                break
    except:
        print("Algo deu errado")
        pass

def verificador7(VERIF):
    concurso = 1200

    JOGOS = []

    while True:
        try:
            if concurso == 1400:
                break
            else:
                response = requests.get(f"https://loteriascaixa-api.herokuapp.com/api/mega-sena/{concurso}", verify=False)
                dezenas = response.json()
                if dezenas["dezenas"]:
                    JOGOS.append(dezenas["dezenas"])
                else:
                    print(concurso)
                    break
                concurso += 1
        except:
            break

    try:
        l1 = VERIF
        for jogo in JOGOS:
            if jogo == l1:
                print("Jogo repetido: ")
                print(jogo)
                break
    except:
        print("Algo deu errado")
        pass

def verificador8(VERIF):
    concurso = 1400

    JOGOS = []

    while True:
        try:
            if concurso == 1550:
                break
            else:
                response = requests.get(f"https://loteriascaixa-api.herokuapp.com/api/mega-sena/{concurso}", verify=False)
                dezenas = response.json()
                if dezenas["dezenas"]:
                    JOGOS.append(dezenas["dezenas"])
                else:
                    print(concurso)
                    break
                concurso += 1
        except:
            break

    try:
        l1 = VERIF
        for jogo in JOGOS:
            if jogo == l1:
                print("Jogo repetido: ")
                print(jogo)
                break
    except:
        print("Algo deu errado")
        pass

def verificador9(VERIF):
    concurso = 1550

    JOGOS = []

    while True:
        try:
            if concurso == 1700:
                break
            else:
                response = requests.get(f"https://loteriascaixa-api.herokuapp.com/api/mega-sena/{concurso}", verify=False)
                dezenas = response.json()
                if dezenas["dezenas"]:
                    JOGOS.append(dezenas["dezenas"])
                else:
                    print(concurso)
                    break
                concurso += 1
        except:
            break

    try:
        l1 = VERIF
        for jogo in JOGOS:
            if jogo == l1:
                print("Jogo repetido: ")
                print(jogo)
                break
    except:
        print("Algo deu errado")
        pass

def verificador10(VERIF):
    concurso = 1700

    JOGOS = []

    while True:
        try:
            if concurso == 1850:
                break
            else:
                response = requests.get(f"https://loteriascaixa-api.herokuapp.com/api/mega-sena/{concurso}", verify=False)
                dezenas = response.json()
                if dezenas["dezenas"]:
                    JOGOS.append(dezenas["dezenas"])
                else:
                    print(concurso)
                    break
                concurso += 1
        except:
            break

    try:
        l1 = VERIF
        for jogo in JOGOS:
            if jogo == l1:
                print("Jogo repetido: ")
                print(jogo)
                break
    except:
        print("Algo deu errado")
        pass
    

def verificador11(VERIF):
    concurso = 1850

    JOGOS = []

    while True:
        try:
            
            
            
            response = requests.get(f"https://loteriascaixa-api.herokuapp.com/api/mega-sena/{concurso}", verify=False)
            dezenas = response.json()
            if dezenas["dezenas"]:
                JOGOS.append(dezenas["dezenas"])
            else:
                print(concurso)
                break
            concurso += 1
        except:
            break

    try:
        l1 = VERIF
        for jogo in JOGOS:
            if jogo == l1:
                print("Jogo repetido: ")
                print(jogo)
                break
    except:
        print("Algo deu errado")
        pass

    print("FIM")
    print(VERIF)
    