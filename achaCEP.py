# Procurar o CEP... Digite o UF, Cidade e Enderenço em Tabela
import os
from sys import displayhook
import time
import pandas
import requests

def achar():
     os.system('cls' if os.name == 'nt' else 'clear') 
     print("\n\033[1;36m   Procurar o seu CEP, ao digitar Cidade e Endereço pode digitar no mínino quatro letras\033[m\n") 
     while True:
          uf = input("\033[1;30;46m   Digite o Estado:\033[m")         
          if not uf.isalpha():
               print ("\033[0;32m Apenas letras são permitidas e obrigatórios!\033[m")                
          else:
               break             
     while True:               
          cidade = input("\033[1;30;46m   Digite a Cidade:\033[m")    
          if not cidade.isalpha():
               print ("\033[0;32m Apenas letras são permitidas e obrigatórios!\033[m") 
          else:
               break
     while True:               
          rua = input("\033[1;30;46m   Digite o Endereço:\033[m")       
          if not rua.isalpha():
               print ("\033[0;32m Apenas letras são permitidas e obrigatórios!\033[m") 
          else:
               break
          
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
            
     cons = input("\033[0;33m  Deseja consultar novamente[S/N]?\033[m").upper()
     if cons == 'S':
          achar()
     else:    
          print("\n\033[1;36m         Feito por Sérgio Renato Steglich - SRSistemas\033[m\n") 
          time.sleep(3)                
     exit()                    
            
achar()
    