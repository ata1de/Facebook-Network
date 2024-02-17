import random
# Abrir o arquivo txt para leitura
with open('facebook.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

def rastrear_caminho(grafo: dict, quadro_distancias: dict, vertice_inicial: int, vertice_final: int) -> [int]:
    caminho = []
    atual = vertice_final

    # PERCORRENDO CAMINHO REVERSO
    while atual != vertice_inicial:
        caminho.insert(0, atual)
        for dados_vizinho in grafo[atual]:
            vizinho, peso = dados_vizinho
            # VERIFICA SE A SOMA DA DIST. DO VIZINHO + O PESO = DISTANCIA DO ATUAL
            if quadro_distancias[atual] == quadro_distancias[vizinho] + peso:
                atual = vizinho
    caminho.insert(0, vertice_inicial)
    return caminho

def dijkstra(grafo: dict, vertice_inicial: int, vertice_final: int) -> tuple:
    # CRIA QUADRO DE DISTANCIAS COM VALORES INFINITOS
    quadro_distancias = {v: float('inf') for v in  range(len(grafo))}
    quadro_distancias[vertice_inicial] = 0
    fila_visita = [(0, vertice_inicial)]

    while fila_visita:
        # USA UMA FILA DE VISITA, ADICIONANDO VIZINHOS COM OS MENORES PESOS
        distancia_atual, vertice_atual = min(fila_visita)
        fila_visita.remove(min(fila_visita))
        for dados_vizinho in grafo[vertice_atual]:
            vizinho, peso = dados_vizinho
            peso_cumulativo = distancia_atual + peso
            if peso_cumulativo < quadro_distancias[vizinho]:
                quadro_distancias[vizinho] = peso_cumulativo
                fila_visita.append((peso_cumulativo, vizinho))

    return rastrear_caminho(grafo, quadro_distancias, vertice_inicial, vertice_final), quadro_distancias[vertice_final]
    
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

trajeto, duracao_conexao = dijkstra(grafo, 0, 3000)

# criação do grafo para a formação da imagem
grafo_imagem = {}
for index in range(len(trajeto)):
    vertice_trajeto =  grafo[trajeto[index]]
    for elementos in vertice_trajeto:
        if index == len(trajeto) - 1:
            break
        if elementos[0] == trajeto[index+1]:
            grafo_imagem[trajeto[index]] = elementos

print(grafo_imagem)
print(trajeto)
print(duracao_conexao)
