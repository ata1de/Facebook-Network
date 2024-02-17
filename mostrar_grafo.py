import networkx as nx
import matplotlib.pyplot as plt
import main
#pip install scipy, matplotlib, networkx


# Função para visualizar o grafo
def visualizar_grafo(grafo, origem, destino):
    G = nx.DiGraph()  # Se o grafo for direcionado, use nx.DiGraph(); se não, use nx.Graph()
    
    # Adiciona os vértices e as arestas ao grafo
    for vertice, vizinhos in grafo.items():
        G.add_edge(vertice, vizinhos[0], weight=vizinhos[1])
        # for vizinho, peso in vizinhos:
        #     G.add_edge(vertice, vizinho, weight=peso)

    # Calcula o menor caminho
    menor_caminho = nx.shortest_path(G, source=origem, target=destino, weight='weight')
    peso_total = nx.shortest_path_length(G, source=origem, target=destino, weight='weight')

    # Posiciona os nós usando o layout Kamada-Kawai
    pos = nx.kamada_kawai_layout(G)
    
    # Obtém as posições dos nós
    pos_labels = {}
    for key, value in pos.items():
        pos_labels[key] = (value[0], value[1] + 0.08)
    
    # Desenha o grafo
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=12, font_weight="bold", arrowsize=20, edge_color="gray", linewidths=1, arrows=True)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    nx.draw_networkx_labels(G, pos_labels)

    # Exibe o menor caminho e o peso total no canto da tela
    plt.text(0.001, 0.001, f'Menor Caminho: {menor_caminho}\nPeso Total: {peso_total}', transform=plt.gca().transAxes)
    
    # Exibe a visualização
    plt.show()

# Chamada da função para visualizar o grafo
visualizar_grafo(main.grafo_imagem, main.vertice_inicial, main.vertice_final)  # Substitua 'A' e 'D' pelos vértices de origem e destino desejados