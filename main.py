import random
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

print(grafo)