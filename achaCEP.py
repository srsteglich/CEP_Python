# Procurar o CEP... Digite o UF, Cidade e Enderenço em Tabela
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
    #### print(" lista ", dic_req)      
    tabela = pandas.DataFrame(dic_req)        
    tabela.rename(columns={'cep':'CEP','logradouro':'Endereço','bairro':'Bairro','localidade':'Cidade','uf':'UF'}, inplace=True)
    tabela.pop('complemento')
    tabela.pop('ibge') 
    tabela.pop('gia')
    tabela.pop('ddd')
    tabela.pop('siafi')
    displayhook(tabela)
            
    cons = input("\033[0;33m  Deseja consultar novamente[S/N]?\033[m]").upper()
    if cons == 'S':
         achar()
    else:    
         print("\n\033[1;36m         Feito por Sérgio Renato Steglich - SRSistemas\033[m\n")                 
    exit()                    
            
achar()
    