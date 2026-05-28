# Importa o módulo csv para ler arquivos CSV
import csv

# Importa o tkinter
import tkinter as tk

# Importa a janela de seleção de arquivos
from tkinter import filedialog

# Cria a janela principal do tkinter
# O .withdraw() esconde a janela principal
janela = tk.Tk()
janela.withdraw()

# Abre o explorador de arquivos para o usuário escolher o CSV
caminho_arquivo = filedialog.askopenfilename(
    title="Selecione o arquivo CSV",
    
    # Tipos de arquivos permitidos
    filetypes=[("Arquivos CSV", "*.csv")]
)

# Verifica se o usuário selecionou um arquivo
if caminho_arquivo:

    # Variável para armazenar o total das vendas
    total_vendas = 0

    # Dicionário para armazenar quantidade vendida de cada produto
    quantidade_produtos = {}

    # Abre o arquivo CSV selecionado
    with open(caminho_arquivo, mode="r", encoding="utf-8") as arquivo:

        # Lê o CSV como dicionário
        leitor = csv.DictReader(arquivo)

        # Percorre cada linha do arquivo
        for linha in leitor:

            # Pega os dados das colunas
            produto = linha["produto"]
            quantidade = int(linha["quantidade"])
            preco = float(linha["preco"])

            # Calcula o valor da venda
            valor_venda = quantidade * preco

            # Soma ao total geral
            total_vendas += valor_venda

            # Verifica se o produto já existe no dicionário
            if produto in quantidade_produtos:

                # Soma a quantidade vendida
                quantidade_produtos[produto] += quantidade

            else:
                # Adiciona o produto no dicionário
                quantidade_produtos[produto] = quantidade

    # Descobre o produto mais vendido
    produto_mais_vendido = max(
        quantidade_produtos,
        key=quantidade_produtos.get
    )

    # Exibe os resultados
    print(f"\nTotal de vendas: R$ {total_vendas:.2f}")

    print(
        f"Produto mais vendido: {produto_mais_vendido} "
        f"({quantidade_produtos[produto_mais_vendido]} unidades)"
    )

else:
    # Caso o usuário não selecione nenhum arquivo
    print("Nenhum arquivo foi selecionado.")