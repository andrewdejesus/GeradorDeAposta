from gerarnumero import gerandonumero6


from gerarnumero import *

if __name__== "__main__":
    while True:
        jogo = input("Quantidade de números: ")
        if jogo == "6":
            print(gerandonumero6(aposta))
            break
        if jogo == "7":
            print(gerandonumero7(aposta))
            break
        if jogo == "8":
            print(gerandonumero8(aposta))
            break
        if jogo == "9":
            print(gerandonumero9(aposta))
            break
        if jogo == "10":
            print(gerandonumero10(aposta))
            break
        if jogo == "11":
            print(gerandonumero11(aposta))
            break
        if jogo == "12":
            print(gerandonumero12(aposta))
            break
        if jogo == "13":
            print(gerandonumero13(aposta))
            break
        if jogo == "14":
            print(gerandonumero14(aposta))
            break
        if jogo == "15":
            print(gerandonumero15(aposta))
            break
        else:
            print("Digite um número de 6 a 15")
