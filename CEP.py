# Digite o CEP e busca o Endereço, a Cidade e o UF
import os
import time
import requests

def buscar():
    os.system('cls' if os.name == 'nt' else 'clear') 
    cep = input("\033[1;30;46m   Digite o seu CEP:\033[m")
    cep = cep.replace("-","").replace(".","").replace(" ","")
    if not cep.isdigit():
        print("\n\033[1;31m    CEP invalido!!! Digite apenas números\033[m ")
        time.sleep(1.5)
        os.system('cls' if os.name == 'nt' else 'clear')        
        buscar()        
    if len(cep) == 8:
        link = f'https://viacep.com.br/ws/{cep}/json/'
        req = requests.get(link)
        dic_req = req.json()
        if 'erro' in dic_req:
            print("\n\033[1;31m     CEP não encontrado.\033[m ")
            time.sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')            
            buscar()
        else:
            rua = dic_req['logradouro']
            comple = dic_req['complemento']            
            bairro = dic_req['bairro']
            cidade = dic_req['localidade']
            uf = dic_req['uf']
            cep = dic_req['cep']
            print(rua,"-", comple," - ", bairro)            
            print(cidade,"-", uf," - CEP:",cep)            
    else:
        print("\n\033[1;31m     CEP invalido!!! Digite com 8 números\033[m ")
        time.sleep(1.5)
        os.system('cls' if os.name == 'nt' else 'clear')      
        buscar()
    cons = input("\033[0;33m  Deseja consultar novamente[S/N]?\033[m]").upper()
    if cons == 'S':
        buscar()
    else:    
        print("\n\033[1;36m         Feito por Sérgio Renato Steglich - SRSistemas\033[m\n")                 
        time.sleep(3.0)
    exit()                    
            
buscar()
    