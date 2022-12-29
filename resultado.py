# script processos_var.py
from threading import Thread, Lock
from multiprocessing import Process
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def verificador(VERIF, concurso):
    
    try:

        while True:
                response = requests.get(f"https://apiloterias.com.br/app/resultado?loteria=megasena&token=daBUAb9LuvqytMq&concurso={concurso}", verify=False)
                dezenas = response.json()
                if concurso == 200:
                    break
                if dezenas["numero_concurso"] == concurso:
                    try:
                        l1 = VERIF
                        
        
                        if l1 == dezenas["dezenas"]:
                            print("Jogo repetido: ")
                            print(l1)
                            break
                    except Exception as e:
                        print(e)
                        pass
                    concurso += 1
                else:
                    break
    except:
        pass        
            

def verificador1(VERIF, concurso):
    
    
    try:
        while True:
                response = requests.get(f"https://apiloterias.com.br/app/resultado?loteria=megasena&token=daBUAb9LuvqytMq&concurso={concurso}", verify=False)
                dezenas = response.json()
                if concurso == 400:
                    break
                if dezenas["numero_concurso"] == concurso:
                    try:
                        l1 = VERIF
                        
                        
                        if l1 == dezenas["dezenas"]:
                            print("Jogo repetido: ")
                            print(l1)
                            break
                    except Exception as e:
                        print(e)
                        pass
                    concurso += 1
                else:
                    break
            
    except:
        pass     

def verificador2(VERIF, concurso):
    
    try:

        while True:
                response = requests.get(f"https://apiloterias.com.br/app/resultado?loteria=megasena&token=daBUAb9LuvqytMq&concurso={concurso}", verify=False)
                dezenas = response.json()
                if concurso == 600:
                    break
                
                if dezenas["numero_concurso"] == concurso:
                    try:
                        l1 = VERIF
                        
                        
                        if l1 == dezenas["dezenas"]:
                            print("Jogo repetido: ")
                            print(l1)
                            break
                    except Exception as e:
                        print(e)
                        pass
                    concurso += 1
                else:
                    break
    except:
        pass


def verificador3(VERIF, concurso):
    
    
    try:
        while True:
                response = requests.get(f"https://apiloterias.com.br/app/resultado?loteria=megasena&token=daBUAb9LuvqytMq&concurso={concurso}", verify=False)
                dezenas = response.json()
                if concurso == 800:
                    break
                
                if dezenas["numero_concurso"] == concurso:
                    try:
                        l1 = VERIF
                        
                        
                        if l1 == dezenas["dezenas"]:
                            print("Jogo repetido: ")
                            print(l1)
                            break
                    except Exception as e:
                        print(e)
                        pass
                    concurso += 1
                else:
                    break
    except:
        pass
            

def verificador4(VERIF, concurso):
    
    
    try:
        while True:
                response = requests.get(f"https://apiloterias.com.br/app/resultado?loteria=megasena&token=daBUAb9LuvqytMq&concurso={concurso}", verify=False)
                dezenas = response.json()
                if concurso == 1000:
                    break
                
                if dezenas["numero_concurso"] == concurso:
                    try:
                        l1 = VERIF
                        
                        
                        if l1 == dezenas["dezenas"]:
                            print("Jogo repetido: ")
                            print(l1)
                            break
                    except Exception as e:
                        print(e)
                        pass
                    concurso += 1
                else:
                    break
    except:
        pass


def verificador6(VERIF, concurso):
    
    
    try:
        while True:
                response = requests.get(f"https://apiloterias.com.br/app/resultado?loteria=megasena&token=daBUAb9LuvqytMq&concurso={concurso}", verify=False)
                dezenas = response.json()
                if concurso == 1200:
                    break
                
                if dezenas["numero_concurso"] == concurso:
                    try:
                        l1 = VERIF
                        
                        
                        if l1 == dezenas["dezenas"]:
                            print("Jogo repetido: ")
                            print(l1)
                            break
                    except Exception as e:
                        print(e)
                        pass
                    concurso += 1
                else:
                    break

    except:
        pass

def verificador7(VERIF, concurso):
    
    
    try:
        while True:
                response = requests.get(f"https://apiloterias.com.br/app/resultado?loteria=megasena&token=daBUAb9LuvqytMq&concurso={concurso}", verify=False)
                dezenas = response.json()
                if concurso == 1400:
                    break
                
                if dezenas["numero_concurso"] == concurso:
                    try:
                        l1 = VERIF
                        
                        
                        if l1 == dezenas["dezenas"]:
                            print("Jogo repetido: ")
                            print(l1)
                            break
                    except Exception as e:
                        print(e)
                        pass
                    concurso += 1
                else:
                    break     
    except:
        pass 

def verificador8(VERIF, concurso):
    
    
    try:
        while True:
                response = requests.get(f"https://apiloterias.com.br/app/resultado?loteria=megasena&token=daBUAb9LuvqytMq&concurso={concurso}", verify=False)
                dezenas = response.json()
                if concurso == 1600:
                    break
                
                if dezenas["numero_concurso"] == concurso:
                    try:
                        l1 = VERIF
                        
                        
                        if l1 == dezenas["dezenas"]:
                            print("Jogo repetido: ")
                            print(l1)
                            break
                    except Exception as e:
                        print(e)
                        pass
                    concurso += 1
                else:
                    break  

    except:
        pass
def verificador9(VERIF, concurso):
    
    try: 

        while True:
                response = requests.get(f"https://apiloterias.com.br/app/resultado?loteria=megasena&token=daBUAb9LuvqytMq&concurso={concurso}", verify=False)
                dezenas = response.json()
                if concurso == 1800:
                    break
                
                if dezenas["numero_concurso"] == concurso:
                    try:
                        l1 = VERIF
                        
                        
                        if l1 == dezenas["dezenas"]:
                            print("Jogo repetido: ")
                            print(l1)
                            break
                    except Exception as e:
                        print(e)
                        pass
                    concurso += 1
                else:
                    break 
    except:
        pass


def verificador10(VERIF, concurso):
    
    
    try:
        while True:
                response = requests.get(f"https://apiloterias.com.br/app/resultado?loteria=megasena&token=daBUAb9LuvqytMq&concurso={concurso}", verify=False)
                dezenas = response.json()
                if concurso == 2000:
                    break
                
                if dezenas["numero_concurso"] == concurso:
                    try:
                        l1 = VERIF
                        
                        
                        if l1 == dezenas["dezenas"]:
                            print("Jogo repetido: ")
                            print(l1)
                            break
                    except Exception as e:
                        print(e)
                        pass
                    concurso += 1
                else:
                    break  
    except:
        pass

def verificador11(VERIF, concurso):
    
    
    try:
        while True:
                response = requests.get(f"https://apiloterias.com.br/app/resultado?loteria=megasena&token=daBUAb9LuvqytMq&concurso={concurso}", verify=False)
                dezenas = response.json()
                if concurso == 2200:
                    break
                
                if dezenas["numero_concurso"] == concurso:
                    try:
                        l1 = VERIF
                        
                        
                        if l1 == dezenas["dezenas"]:
                            print("Jogo repetido: ")
                            print(l1)
                            break
                    except Exception as e:
                        print(e)
                        pass
                    concurso += 1
                else:
                    break  
    except:
        pass


def verificador12(VERIF, concurso):
    
    
    try:
        while True:
                response = requests.get(f"https://apiloterias.com.br/app/resultado?loteria=megasena&token=daBUAb9LuvqytMq&concurso={concurso}", verify=False)
                dezenas = response.json()
                if concurso == 2400:
                    break
                
                if dezenas["numero_concurso"] == concurso:
                    try:
                        l1 = VERIF
                        
                        
                        if l1 == dezenas["dezenas"]:
                            print("Jogo repetido: ")
                            print(l1)
                            break
                    except Exception as e:
                        print(e)
                        pass
                    concurso += 1
                    
                else:
                    break  
    except:
        pass

def verificador13(VERIF, concurso):
    
    
    try:
        while True:
                response = requests.get(f"https://apiloterias.com.br/app/resultado?loteria=megasena&token=daBUAb9LuvqytMq&concurso={concurso}", verify=False)
                dezenas = response.json()
                
                if dezenas["numero_concurso"] == concurso:
                    try:
                        l1 = VERIF
                        
                        
                        if l1 == dezenas["dezenas"]:
                            print("Jogo repetido: ")
                            print(l1)
                            break
                    except Exception as e:
                        print(e)
                        pass
                    concurso += 1
                    
                else:
                    break  
    except:
        pass

