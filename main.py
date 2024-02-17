import random
import mostrar_grafo
import algoritmo

# Abrir o arquivo txt para leitura
with open('facebook.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
   
# criar o grafo 
grafo = {}

# Iterar sobre as linhas do arquivo
for linha in linhas:
    # Divindo em chave e valor
    chave, valor = linha.split()  
    # gerando um peso de forma aleatória
    numero_aleatorio = random.randint(1, 100)
    # Adicionar ao dicionário como uma tupla
    if int(chave) in grafo:
        grafo[int(chave)].append((int(valor), numero_aleatorio))
    else:
        grafo[int(chave)] = [(int(valor), numero_aleatorio)]

    # CRIA A RELAÇÃO AO CONTRÁRIO TAMBÉM, OU SEJA, GRAFO NÃO DIRECIONAL
    if int(valor) in grafo:
        grafo[int(valor)].append((int(chave), numero_aleatorio))
    else:
        grafo[int(valor)] = [(int(chave), numero_aleatorio)]

vertice_inicial = 0
vertice_final = 1500
trajeto, duracao_conexao = algoritmo.dijkstra(grafo, vertice_inicial, vertice_final)

# criação do grafo para a formação da imagem
grafo_imagem = {}
for index in range(len(trajeto)):
    vertice_trajeto =  grafo[trajeto[index]]
    for elementos in vertice_trajeto:
        if index == len(trajeto) - 1:
            break
        if elementos[0] == trajeto[index+1]:
            grafo_imagem[trajeto[index]] = elementos

# print(grafo_imagem)
# print(trajeto)
# print(duracao_conexao)
origem, destino = mostrar_grafo.interface_inicial()
mostrar_grafo.visualizar_grafo(grafo_imagem, origem, destino, trajeto, duracao_conexao)
# mostrar_grafo.visualizar_grafo(grafo_imagem, vertice_inicial, vertice_final)
