# Importa a classe datetime do módulo datetime
# Ela será usada para pegar a data e hora atual
from datetime import datetime


# Função responsável por registrar logs
def registrar_log(tipo, mensagem):

    # Obtém a data e hora atual
    agora = datetime.now()

    # Formata a data/hora no padrão:
    # dia/mês/ano hora:minuto:segundo
    timestamp = agora.strftime("%d/%m/%Y %H:%M:%S")

    # Monta a mensagem final do log
    # Exemplo:
    # [21/05/2026 19:30:15] [INFO] Sistema iniciado
    linha_log = f"[{timestamp}] [{tipo}] {mensagem}\n"

    # Abre o arquivo "logs.txt"
    # "a" significa APPEND:
    # adiciona novas mensagens sem apagar as antigas
    with open("logs.txt", "a", encoding="utf-8") as arquivo:

        # Escreve a linha dentro do arquivo
        arquivo.write(linha_log)

    # Exibe confirmação no terminal
    print("Log registrado com sucesso!")


# Registrando alguns exemplos de log

registrar_log("INFO", "Sistema iniciado")
registrar_log("WARNING", "Memória quase cheia")
registrar_log("ERROR", "Falha ao conectar ao banco de dados")