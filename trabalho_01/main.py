# Configurar as importações
import sys

# Configurar leitura dos parâmetros
params = sys.argv[1:]

# Lendo os parâmetros
for text in params:

    # Verificando o tipo de parâmetro
    if text == 'read':
        try:
            # Lendo o nome do arquivo no console e armazenando na variável
            arquivo = sys.argv[2]

            # Abrindo o arquivo
            arq = open(arquivo, 'r')
            lines = arq.readlines()

            # Configurando o grafo n
            grafo_n = int(lines[0])

            # Configurando os vértices do grafo
            vertices = lines[1:]

            # 0, 2, 4
            matriz = []

            # Linha
            for i in range(grafo_n):
                linha = []
                # Coluna
                for j in range(grafo_n):
                    if (j == int(vertices[i][0])):
                        linha.append(int(vertices[i][4]))
                    else:
                        linha.append(0)
                matriz.append(linha)
            
            print(matriz)

        except FileNotFoundError as err:
            # Tratando o erro de arquivo não encontrado
            print(f"O arquivo \"{arquivo}\" não foi encontrado")
            break

        except Exception as err:
            # Tratando erros gerais
            print("Ocorreu um erro :", err)
            break

    try:
        # Verificando o tipo de parâmetro
        if text == 'show':

            # Lendo o tipo de matriz que será mostrada
            tipo = sys.argv[4]
            
            # Tratando os tipos de visualizações permitidas
            if tipo == '-li':

                # Printando a lista de incidências         
                print('Lista de incidências')

            elif tipo == '-mi':
                # Printando a matriz de incidências
                print('Matriz de incidências')

            else:
                # Printando erro
                raise Exception(f'Tipo de visualização \"{tipo}\" inválida')

    except Exception as err:
        print(err)


#Tipo de comandos aceitos

# .\main.py read <arquivo> show <tipo>
# show <tipo> : -li ou -mi