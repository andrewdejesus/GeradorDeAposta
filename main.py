from resultados import *
import threading
from gerarnumero import *
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if __name__== "__main__":
    
    jogo = input("Quantidade de números: ")
    if jogo == "6":
        VERIF = gerandonumero6(aposta)
            
        try:
            t1 = threading.Thread(target=verificador1, args=[VERIF])
            t2 = threading.Thread(target=verificador2, args=[VERIF])
            t3 = threading.Thread(target=verificador3, args=[VERIF])
            t4 = threading.Thread(target=verificador4, args=[VERIF])
            t5 = threading.Thread(target=verificador5, args=[VERIF])
            t6 = threading.Thread(target=verificador6, args=[VERIF])
            t7 = threading.Thread(target=verificador7, args=[VERIF])
            t8 = threading.Thread(target=verificador8, args=[VERIF])
            t9 = threading.Thread(target=verificador9, args=[VERIF])
            t10 = threading.Thread(target=verificador10, args=[VERIF])
            t11 = threading.Thread(target=verificador11, args=[VERIF])
            t1.start()
            t2.start()
            t3.start()
            t4.start()
            t5.start()
            t6.start()
            t7.start()
            t8.start()
            t9.start()
            t10.start()
            t11.start()
            print("Comparando jogos...")
        except Exception as e:
            print(e)
            
            
    if jogo == "7":
        print(gerandonumero7(aposta))
            
    if jogo == "8":
        print(gerandonumero8(aposta))
            
    if jogo == "9":
        print(gerandonumero9(aposta))
            
    if jogo == "10":
        print(gerandonumero10(aposta))
            
    if jogo == "11":
        print(gerandonumero11(aposta))
            
    if jogo == "12":
        print(gerandonumero12(aposta))
            
    if jogo == "13":
        print(gerandonumero13(aposta))
            
    if jogo == "14":
        print(gerandonumero14(aposta))
            
    if jogo == "15":
        print(gerandonumero15(aposta))
            
