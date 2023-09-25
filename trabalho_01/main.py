# Configurar as importações
import sys
import os

def calcula_matriz(arquivo):
    # declaração da matriz inicial auxiliar vazia
    matriz = []

    # Abre o arquivo para leitura
    
    with open(arquivo, "r") as arquivo:
        # Lê o valor da primeira linha (quantidade de vertices) e o converte para int
        num_vertices = int(arquivo.readline().strip())

        # Lê o restante das linhas do arquivoos converte para int e os adiciona na matriz auxiliar
        for linha in arquivo:
            valores = linha.split()
            valores = [int(valor) for valor in valores]
            if valores != []:
                matriz.append(valores)

        # Declaração e preenchimento da matriz ponderado com zeros com base na quantidade de vertices
        matriz_ponderada = [[0 for i in range(num_vertices)] for i in range(num_vertices)]
        
        # Preenchimento da matriz ponderada com os valores da matriz lida
        for origem, destino, peso in matriz:
            matriz_ponderada[origem - 1][destino - 1] = peso
        return matriz_ponderada, num_vertices

def imprime_matriz(matriz_ponderada, num_vertices):
    # Impressão da matriz ponderada
    # Imprime o cabeçalho das colunas
    print("Vertices", num_vertices)
    print("   ", end="")
    for i in range(1, num_vertices + 1):
        print(f"{i:2d} ", end="")
    print()

    # Imprime as linhas da matriz
    for i in range(num_vertices):
        # Imprime o cabeçalho das linhas
        print(f"{i + 1:2d} ", end="")
        # Imprime os pesos das arestas
        for j in range(num_vertices):
            print(f"{matriz_ponderada[i][j]:2d} ", end="")
        print()

# Configurar leitura dos parâmetros
params = sys.argv[1:]

# Lendo os parâmetros
for text in params:

    # Verificando o tipo de parâmetro
    if text == 'read':
        try:
            # Lendo o nome do arquivo no console e armazenando na variável
            arquivo = sys.argv[2]

        except FileNotFoundError as err:
            # Tratando o erro de arquivo não encontrado
            print(f"O arquivo \"{arquivo}\" não foi encontrado")
            break

    try:
        # Verificando o tipo de parâmetro
        if text == 'show':

            # Lendo o tipo de matriz que será mostrada
            tipo = sys.argv[4]
            
            # Tratando os tipos de visualizações permitidas
            if tipo == '-mi':
                # Printando a matriz de incidências
                print('Matriz de pesos')

                # Abrindo o arquivo
                matriz, num_vertices = calcula_matriz(arquivo)

                # Imprimir matriz 
                imprime_matriz(matriz, num_vertices)

            else:
                # Printando erro
                raise Exception(f'Tipo de visualização \"{tipo}\" inválida')

    except Exception as err:
        print(err)

#Tipo de comandos aceitos

# .\main.py read <arquivo> show <tipo>
# show <tipo> : -li ou -mi