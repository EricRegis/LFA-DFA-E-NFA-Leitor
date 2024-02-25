import pandas as pd

def entra_dfa(nome):
    # Ler o arquivo de texto
    with open(nome, 'r') as file:
        lines = file.readlines()

    # Processar cada linha do arquivo
    table_data = []
    items_with_asterisk = []

    for line in lines:
        # Remover espaços em branco no início e no final da linha
        line = line.strip()

        # Dividir a linha pelos espaços em branco para obter os elementos
        elements = line.split()

        # Iterar sobre cada elemento na linha
        cleaned_elements = []
        for element in elements:
            # Remover asterisco (*) e maior que (>)
            cleaned_element = element.replace('*', '').replace('>', '')
            cleaned_elements.append(cleaned_element)

            # Verificar se o elemento contém um asterisco (*)
            if '*' in element:
                # Adicionar o elemento à lista de itens com asterisco
                items_with_asterisk.append(cleaned_element)

        # Adicionar os elementos limpos à lista de dados da tabela
        table_data.append(cleaned_elements)

    # Criar um DataFrame usando a biblioteca pandas
    df = pd.DataFrame(table_data)

    return df, items_with_asterisk

def entra_teste(end_teste):
    # Ler o arquivo de entrada
    with open(end_teste, 'r') as file:
        lines = file.readlines()

    # Criar uma lista para armazenar as listas de dígitos
    lists_of_digits = []

    # Processar cada linha do arquivo
    for line in lines:
        # Remover espaços em branco no início e no final da linha
        line = line.strip()

        # Criar uma lista de dígitos para cada caractere na linha
        digit_list = [int(digit) for digit in line]

        # Adicionar a lista de dígitos à lista principal
        lists_of_digits.append(digit_list)

    return lists_of_digits

def aceita(matriz_dfa, final, lista_testes, arquivo_saida):
    with open(arquivo_saida, 'w') as arquivo:
        for teste in lista_testes:
            estado_atual = 'q0'
            for input_value in teste:
                # Encontra o índice do estado atual na tabela DFA
                idx_estado_atual = matriz_dfa.index[matriz_dfa.iloc[:, 0] == estado_atual][0]
                
                # Verifica a transição para o próximo estado com base no valor de entrada
                proximo_estado = matriz_dfa.iloc[idx_estado_atual, input_value + 1]
                
                # Atualiza o estado atual
                estado_atual = proximo_estado

            if avalia(estado_atual, final):
                print("Aceita", file=arquivo)
            else:
                print("Rejeita", file=arquivo)

def avalia(estadoFinal, estadosFinais):
    if estadoFinal in estadosFinais:
        return True
    else:
        return False

# Carregar dados do DFA e dos testes
df_result, listaFinal = entra_dfa('/Users/Usuario/Documents/TrabalhoLFA/ex_dfa02.txt')
lista_testes = entra_teste('/Users/Usuario/Documents/TrabalhoLFA/strings_test.txt')

# Nome do arquivo de saída
nome_arquivo_saida = '/Users/Usuario/Documents/TrabalhoLFA/resultado1.txt'

# Executar os testes e salvar os resultados no arquivo
aceita(df_result, listaFinal, lista_testes, nome_arquivo_saida)

print(f"Resultados dos testes foram salvos em: {nome_arquivo_saida}")
