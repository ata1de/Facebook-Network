import random
# Abrir o arquivo txt para leitura
with open('facebook.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

# criar o grafo 
grafo = {}

def dijkstra(grafo, vertice_inicial, vertice_final):
    quadro_distancias = {v: float('inf') for v in  range(len(grafo))}
    quadro_distancias[vertice_inicial] = 0
    fila_visita = [(0, vertice_inicial)]

    while fila_visita:
        distancia_atual, vertice_atual = min(fila_visita)
        fila_visita.remove(min(fila_visita))
        for dados_vizinho in grafo[vertice_atual]:
            vizinho, peso = dados_vizinho
            peso_cumulativo = distancia_atual + peso
            if peso_cumulativo < quadro_distancias[vizinho]:
                quadro_distancias[vizinho] = peso_cumulativo
                fila_visita.append((peso_cumulativo, vizinho))
    print(quadro_distancias)

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


# print(grafo)

dijkstra(grafo, 0, 18)