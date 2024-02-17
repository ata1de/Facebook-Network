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