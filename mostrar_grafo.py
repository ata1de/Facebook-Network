import networkx as nx
import matplotlib.pyplot as plt
import main


# Função para visualizar o grafo
def visualizar_grafo(grafo):
    G = nx.DiGraph()  # Se o grafo for direcionado, use nx.DiGraph(); se não, use nx.Graph()
    
    # Adiciona os vértices e as arestas ao grafo
    for vertice, vizinhos in grafo.items():
        for vizinho, peso in vizinhos.items():
            G.add_edge(vertice, vizinho, weight=peso)

    # Posiciona os nós usando o layout Kamada-Kawai
    pos = nx.kamada_kawai_layout(G)
    
    # Obtém as posições dos nós
    pos_labels = {}
    for key, value in pos.items():
        pos_labels[key] = (value[0], value[1] + 0.08)

    # Desenha o grafo
    nx.draw_networkx(G, pos, with_labels=True)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    nx.draw_networkx_labels(G, pos_labels)
    
    # Exibe a visualização
    plt.show()

# Chamada da função para visualizar o grafo
visualizar_grafo(main.grafo_imagem)