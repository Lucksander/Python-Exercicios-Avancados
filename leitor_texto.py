# Programa que lê um arquivo .txt e exibe seu conteúdo na tela

# Solicita ao usuário o nome do arquivo
nome_arquivo = input("Digite o nome do arquivo (.txt): ")

try:
    # Abre o arquivo no modo leitura ("r")
    arquivo = open(nome_arquivo, "r", encoding="utf-8")

    # Lê todo o conteúdo do arquivo
    conteudo = arquivo.read()

    # Exibe o conteúdo na tela
    print("\n--- Conteúdo do Arquivo ---")
    print(conteudo)

    # Fecha o arquivo
    arquivo.close()

# Trata o erro caso o arquivo não exista
except FileNotFoundError:
    print("Erro: arquivo não encontrado.")

# Trata outros possíveis erros
except Exception as erro:
    print("Ocorreu um erro:", erro)