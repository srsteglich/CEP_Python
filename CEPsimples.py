# Digite o CEP e busca o Endereço, a Cidade e o UF
import os
import time
from pycep import PyCep

def simpCep():
    os.system('cls' if os.name == 'nt' else 'clear') 
    cep = input("\033[1;30;46m   Digite o seu CEP:\033[m")
    cep = cep.replace("-","").replace(".","").replace(" ","")
    if not cep.isdigit():
        print("\n\033[1;31m    CEP invalido!!! Digite apenas números\033[m ")
        time.sleep(1.5)
        os.system('cls' if os.name == 'nt' else 'clear')        
        simpCep()        
    if len(cep) == 8:
        cep = PyCep(cep)
        retorno = cep.dadosCep        
        if 'erro' in retorno:
            print("\n\033[1;31m     CEP não encontrado.\033[m ")
            time.sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')            
            simpCep()
        else:
            rua = retorno['logradouro']
            comple = retorno['complemento']            
            bairro = retorno['bairro']
            cidade = retorno['localidade']
            uf = retorno['uf']
            cep = retorno['cep']
            print(rua,"-", comple," - ", bairro)            
            print(cidade,"-", uf," - CEP:",cep)            
    else:
        print("\n\033[1;31m     CEP invalido!!! Digite com 8 números\033[m ")
        time.sleep(1.5)
        os.system('cls' if os.name == 'nt' else 'clear')      
        simpCep()
    cons = input("\033[0;33m  Deseja consultar novamente[S/N]?\033[m]").upper()
    if cons == 'S':
        simpCep()
    else:    
        print("\n\033[1;36m         Feito por Sérgio Renato Steglich - SRSistemas\033[m\n")                 
    exit()                    
            
simpCep()
