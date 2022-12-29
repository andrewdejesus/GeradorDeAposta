
import threading
from gerarnumero import *
import urllib3
from resultado import *
from datetime import *

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if __name__== "__main__":
    
    jogo = input("Quantidade de números: ")
    if jogo == "6":
        VERIF = gerandonumero6(aposta)
        atual = datetime.now()

        t1 = atual.strftime("%H:%M:%S")
        print(f"Comparando jogos...{t1}")
        try:
            t1 = threading.Thread(target=verificador, args=(VERIF,1))
            t2 = threading.Thread(target=verificador1, args=(VERIF,200))
            t3 = threading.Thread(target=verificador2, args=(VERIF,400))
            t4 = threading.Thread(target=verificador3, args=(VERIF,600))
            t5 = threading.Thread(target=verificador4, args=(VERIF,800))
            t6 = threading.Thread(target=verificador6, args=(VERIF,1000))
            t7 = threading.Thread(target=verificador7, args=(VERIF,1200))
            t8 = threading.Thread(target=verificador8, args=(VERIF,1400))
            t9 = threading.Thread(target=verificador9, args=(VERIF,1600))
            t10 = threading.Thread(target=verificador10, args=(VERIF,1800))
            t11 = threading.Thread(target=verificador11, args=(VERIF,2000))
            t12 = threading.Thread(target=verificador12, args=(VERIF,2200))
            t13 = threading.Thread(target=verificador13, args=(VERIF,2400))
   
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
            t12.start()
            t13.start()

            t1.join()
            t2.join()
            t3.join()
            t4.join()
            t5.join()
            t6.join()
            t7.join()
            t8.join()
            t9.join()
            t10.join()
            t11.join()
            t12.join()
            t13.join()

            atual = datetime.now()

            t2 = atual.strftime("%H:%M:%S")
            print(VERIF)
            print(f"fim: {t2}")
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
            
