import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
#pip install scipy, matplotlib, networkx

# Função para visualizar o grafo
def visualizar_grafo(grafo,menor_caminho, peso_total):
    G = nx.DiGraph()  # Se o grafo for direcionado, use nx.DiGraph(); se não, use nx.Graph()
    
    # Adiciona os vértices e as arestas ao grafo
    for vertice, vizinhos in grafo.items():
        G.add_edge(vertice, vizinhos[0], weight=vizinhos[1])
        # for vizinho, peso in vizinhos:
        #     G.add_edge(vertice, vizinho, weight=peso)

    # Calcula o menor caminho
    # menor_caminho = nx.shortest_path(G, source=origem, target=destino, weight='weight')
    # peso_total = nx.shortest_path_length(G, source=origem, target=destino, weight='weight')

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

def criar_janela():
    # Criando a interface
    root = tk.Tk()
    root.title("Visualizador de Grafo")

    label_origem = tk.Label(root, text="Vértice Inicial:")
    label_origem.grid(row=0, column=0, padx=5, pady=5)
    var_origem = tk.StringVar()
    entry_origem = tk.Entry(root, textvariable=var_origem)
    entry_origem.grid(row=0, column=1, padx=5, pady=5)

    label_destino = tk.Label(root, text="Vértice Final:")
    label_destino.grid(row=1, column=0, padx=5, pady=5)
    var_destino = tk.StringVar()
    entry_destino = tk.Entry(root, textvariable=var_destino)
    entry_destino.grid(row=1, column=1, padx=5, pady=5)

    button_enviar = tk.Button(root, text="Enviar", command=lambda: enviar_inputs(root, var_origem, var_destino))
    button_enviar.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    return root, var_origem, var_destino

def enviar_inputs(root, var_origem, var_destino):
    origem = var_origem.get()
    destino = var_destino.get() # Fecha a janela após enviar os inputs
    return origem, destino

def interface_inicial():
    root, var_origem, var_destino = criar_janela()
    root.mainloop()
    # Retorna os valores de origem e destino após fechar a janela
    return enviar_inputs(root, var_origem, var_destino)

# Agora, a função interface_inicial() retornará os valores de origem e destino
# Chamada da função para visualizar o grafo
# visualizar_grafo(main.grafo_imagem, main.vertice_inicial, main.vertice_final)  # Substitua 'A' e 'D' pelos vértices de origem e destino desejados