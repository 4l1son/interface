from projetoMD.LIB.interface import *
from projetoMD.LIB.arquivo import  *
from projetoMD.resposta import resolucao
from time import sleep

arq = 'definições.txt'
arq1 = 'exercicios.txt'
arq2 = 'reposta.py'
if not arqExiste(arq):
    criarrArquivo(arq)
    criarrArquivo(arq1)
    criarrArquivo(arq2)

while True:
    resposta = menu(['DEFINIÇÕES','EXERCICIOS','RESPOSTA DOS EXERCICIOS','SAIR'])
    if resposta == 1:
        lerArquivo(arq)
        sleep(5)
    elif resposta == 2:
        lerArquivo(arq1)
        sleep(5)
    if resposta == 3:
         print(resolucao())
         sleep(5)

    if resposta == 4:
        cabeçalho('Saindo do sistema...')
        break
    if resposta > 4:
        print('\033[31mERRO!DIGITE UMA OPÇÃO VALIDA!\033[m')
    sleep(2)



