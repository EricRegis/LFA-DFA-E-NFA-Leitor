import pandas as pd

def le_arquivo(nome):
    with open(nome, 'r') as arquivo:
        linhas = arquivo.readlines()
    return linhas

def processa_tabela(linhas):
    tabela = {}
    for linha in linhas:
        partes = linha.split()
        if len(partes) < 3:
            continue  # Ignora linhas que não têm todos os elementos esperados
        origem = partes[0]
        transicoes_0 = partes[1].strip('{}').split(',')  # Remove as chaves e divide os estados
        transicoes_1 = partes[2].strip('{}').split(',')  # Remove as chaves e divide os estados
        for estado_destino in transicoes_0:
            if (origem, '0') not in tabela:
                tabela[(origem, '0')] = [estado_destino]
            else:
                tabela[(origem, '0')].append(estado_destino)
        for estado_destino in transicoes_1:
            if (origem, '1') not in tabela:
                tabela[(origem, '1')] = [estado_destino]
            else:
                tabela[(origem, '1')].append(estado_destino)
    return tabela

def epsilon_fecho(estado, transicoes):
    fecho = set()
    fecho.add(estado)
    if (estado, 'ε') in transicoes:
        for prox_estado in transicoes[(estado, 'ε')]:
            fecho |= epsilon_fecho(prox_estado, transicoes)
    return fecho

def transicao(estado, entrada, transicoes):
    proximos_estados = set()
    if (estado, entrada) in transicoes:
        proximos_estados.update(transicoes[(estado, entrada)])
    return proximos_estados

def construir_dfa(estado_inicial, transicoes):
    estados_dfa = []
    transicoes_dfa = {}
    estados_novos = []

    estado_inicial_dfa = frozenset(epsilon_fecho(estado_inicial, transicoes))
    estados_dfa.append(estado_inicial_dfa)
    estados_novos.append(estado_inicial_dfa)

    while estados_novos:
        estado_atual = estados_novos.pop(0)

        for entrada in entradas:
            proximos_estados = set()
            for estado in estado_atual:
                proximos_estados |= transicao(estado, entrada, transicoes)
            proximos_estados_fechados = set()
            for estado in proximos_estados:
                proximos_estados_fechados |= epsilon_fecho(estado, transicoes)

            proximos_estados_fechados = frozenset(proximos_estados_fechados)
            transicoes_dfa[(estado_atual, entrada)] = proximos_estados_fechados

            if proximos_estados_fechados not in estados_dfa:
                estados_dfa.append(proximos_estados_fechados)
                estados_novos.append(proximos_estados_fechados)

    return estados_dfa, transicoes_dfa

def aceita_dfa(estados_finais, lista_testes, transicoes_dfa, arquivo_saida):
    with open(arquivo_saida, 'w') as arquivo:
        for teste in lista_testes:
            estado_atual = frozenset([estado_inicial])
            aceito = False  # Variável para controlar se o teste foi aceito ou não
            for entrada in teste:
                if (estado_atual, entrada) not in transicoes_dfa:
                    break  # Interrompe o teste atual se a transição não for encontrada
                estado_atual = transicoes_dfa[(estado_atual, entrada)]
            if any(estado in estados_finais for estado in estado_atual):
                aceito = True
            if aceito:
                arquivo.write("aceita\n")
            else:
                arquivo.write("não-aceita\n")

# Leitura dos arquivos de entrada
linhas_tabela_nfa = le_arquivo('/Users/Usuario/Documents/TrabalhoLFA/ex_nfa01.txt')
linhas_tabela_epsilon_nfa = le_arquivo('/Users/Usuario/Documents/TrabalhoLFA/ex_epsilon_nfa.txt')
linhas_testes = le_arquivo('/Users/Usuario/Documents/TrabalhoLFA/strings_test.txt')

# Processamento da tabela de transição do NFA
tabela_nfa = processa_tabela(linhas_tabela_nfa)
tabela_epsilon_nfa = processa_tabela(linhas_tabela_epsilon_nfa)

# Determinação dos estados e entradas
estados = set()
entradas = set()
for (estado, entrada) in tabela_nfa.keys():
    estados.add(estado)
    if entrada != 'ε':
        entradas.add(entrada)

# Construção do DFA a partir do NFA
estado_inicial = 'q0'
estados_dfa_nfa, transicoes_dfa_nfa = construir_dfa(estado_inicial, tabela_nfa)

# Construção do DFA a partir do ε-NFA
estados_dfa_epsilon_nfa, transicoes_dfa_epsilon_nfa = construir_dfa(estado_inicial, tabela_epsilon_nfa)

# Definição dos estados finais do NFA
estados_finais_nfa = {'q3', 'q4'}  # Ajuste conforme necessário

# Definição dos estados finais do DFA (estados que contêm pelo menos um estado final do NFA)
estados_finais_dfa_nfa = set()
for estado_dfa in estados_dfa_nfa:
    if any(estado_nfa in estados_finais_nfa for estado_nfa in estado_dfa):
        estados_finais_dfa_nfa.add(estado_dfa)

# Definição dos estados finais do ε-NFA
estados_finais_epsilon_nfa = {'q3', 'q4'}  # Ajuste conforme necessário

# Definição dos estados finais do DFA (estados que contêm pelo menos um estado final do ε-NFA)
estados_finais_dfa_epsilon_nfa = set()
for estado_dfa in estados_dfa_epsilon_nfa:
    if any(estado_nfa in estados_finais_epsilon_nfa for estado_nfa in estado_dfa):
        estados_finais_dfa_epsilon_nfa.add(estado_dfa)

# Execução do DFA construído a partir do NFA nos testes e escrita dos resultados no arquivo de saída
aceita_dfa(estados_finais_dfa_nfa, linhas_testes, transicoes_dfa_nfa, '/Users/Usuario/Documents/TrabalhoLFA/resultado2_nfa.txt')

# Execução do DFA construído a partir do ε-NFA nos testes e escrita dos resultados no arquivo de saída
aceita_dfa(estados_finais_dfa_epsilon_nfa, linhas_testes, transicoes_dfa_epsilon_nfa, '/Users/Usuario/Documents/TrabalhoLFA/resultado2_epsilon_nfa.txt')

print("Conversões concluídas. Resultados salvos em 'resultado2_nfa.txt' e 'resultado2_epsilon_nfa.txt'.")
