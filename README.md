# LFA-DFA-E-NFA-Leitor
# README
# Sobre o Código do Item 1

Este é um programa Python para processar autômatos finitos determinísticos (DFAs) e realizar testes de aceitação com base em cadeias de entrada.

## Pré-requisitos

- **Sistema Operacional:** Qualquer sistema operacional que suporte Python.
- **Python:** Versão 3.x ou superior.
- **Bibliotecas Python:** Pandas.

## Como Compilar/Executar

1. Certifique-se de ter o Python instalado. Se não tiver, você pode baixá-lo e instalá-lo no site oficial: [Python.org](https://www.python.org/downloads/).

2. Instale a biblioteca pandas executando o seguinte comando no terminal ou prompt de comando:
    ```
    pip install pandas
    ```

3. Baixe o código fonte fornecido (`main.py`) e o arquivo de entrada (`ex_dfa02.txt` e `strings_test.txt`) no mesmo diretório.

4. Abra um terminal ou prompt de comando e navegue até o diretório onde os arquivos estão localizados.

5. Execute o programa Python com o seguinte comando:
    ```
    python main.py
    ```

6. O programa executará os testes e salvará os resultados em um arquivo de saída chamado `resultado1.txt` no mesmo diretório.

7. Após a execução, você pode verificar os resultados no arquivo `resultado1.txt`.

## Observações

Certifique-se de fornecer o caminho correto para os arquivos de entrada `ex_dfa02.txt` e `strings_test.txt` quando solicitado.

Para mais informações sobre o funcionamento do programa, consulte os comentários no código fonte (`main.py`).

#Sobre o Código do Item 2

Este é um programa Python para converter um Autômato Finito Não-determinístico (NFA) em um Autômato Finito Determinístico (DFA) e realizar testes de aceitação com base em cadeias de entrada.

## Pré-requisitos

- **Sistema Operacional:** Qualquer sistema operacional que suporte Python.
- **Python:** Versão 3.x ou superior.
- **Bibliotecas Python:** Pandas.

## Como Compilar/Executar

1. Certifique-se de ter o Python instalado. Se não tiver, você pode baixá-lo e instalá-lo no site oficial: [Python.org](https://www.python.org/downloads/).

2. Instale a biblioteca pandas executando o seguinte comando no terminal ou prompt de comando:
    ```
    pip install pandas
    ```

3. Baixe o código fonte fornecido (`main.py`) e os arquivos de entrada necessários (`ex_nfa01.txt` e `strings_test.txt`) no mesmo diretório.

4. Abra um terminal ou prompt de comando e navegue até o diretório onde os arquivos estão localizados.

5. Execute o programa Python com o seguinte comando:
    ```
    python main.py
    ```

6. O programa converterá o NFA em DFA e salvará os resultados dos testes em um arquivo de saída chamado `resultado2.txt` no mesmo diretório.

7. Após a execução, você pode verificar os resultados no arquivo `resultado2.txt`.

## Observações

- Certifique-se de fornecer o caminho correto para os arquivos de entrada `ex_nfa01.txt` e `strings_test.txt` quando solicitado.
- Você pode ajustar os estados finais do NFA no código conforme necessário, na variável `estados_finais`.
- O programa imprimirá uma mensagem indicando a conclusão da conversão e a localização dos resultados.

Para mais informações sobre o funcionamento do programa, consulte os comentários no código fonte (`main.py`).
