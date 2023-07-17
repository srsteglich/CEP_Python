# Procurar o CEP... Digite o UF, Cidade e Enderenço
import os
from sys import displayhook
import time
import pandas
import requests

def achar():
    os.system('cls' if os.name == 'nt' else 'clear') 
    uf = input("\033[1;30;46m   Digite o Estado:\033[m")
    cidade = input("\033[1;30;46m   Digite a Cidade:\033[m")    
    rua = input("\033[1;30;46m   Digite o Endereço:\033[m")        
    link = f'https://viacep.com.br/ws/{uf}/{cidade}/{rua}/json/'
    req = requests.get(link)
    dic_req = req.json()    
    print("Cidade      -  UF  -  CEP         -    Endereço           -   Bairro")
    for i in dic_req:
        print(i['localidade'],"-",i['uf']," ", i['cep'],"-", i['logradouro']," - ", i['bairro'])
            
    cons = input("\033[0;33m  Deseja consultar novamente[S/N]?\033[m]").upper()
    if cons == 'S':
         achar()
    else:    
         print("\n\033[1;36m         Feito por Sérgio Renato Steglich - SRSistemas\033[m\n")                 
    exit()                    
            
achar()
    