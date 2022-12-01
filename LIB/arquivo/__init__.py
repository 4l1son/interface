from projetoMD.LIB.interface import *
def arqExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def criarrArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação de arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')

def lerArquivo(nome):
    try:
        a = open(nome,'rt', encoding='utf-8')

    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('Definição de conjunto')
        print(a.read())
