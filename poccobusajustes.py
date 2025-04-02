

# Função para gerar a matriz de assentos de forma dinâmica
def gerar_matriz_assentos():
    matriz = []

    # Primeira linha: motorista e corredor
    matriz.append(["Mot", "Corr", "Corr", "Corr", "Corr"])

    # Gerar as demais fileiras dinamicamente
    assento = 1
    for _ in range(12):  # 12 fileiras
        linha = []
        for j in range(5):  # 5 colunas
            if j == 2:  # Corredor no meio
                linha.append("Corr")
            else:
                linha.append(f"A{assento:02}")  # Formata "A01", "A02", etc.
                assento += 1
        matriz.append(linha)

    return matriz
print("\n")

# Função para exibir o mapa atual dos assentos com emojis coloridos
def mostrar_assentos_coloridos(matriz):
    # Exibir a legenda
    print("\n")
    print("Legenda:\n")
    print("🟦 Mot - Motorista")
    print("⬜ Corr - Corredor (Indisponivel para venda)")
    print("🟩 Livre - Assento disponivel")
    print("⬛ Indisponivel - Assento vendido")
    print()

    # Exibir a matriz de assentos com cores
    for linha in matriz:
        linha_colorida = []  # Inicializar a linha colorida
        for assento in linha:
            if assento == "Mot":
                linha_colorida.append("🟦 Mot ")  # Azul para o motorista
            elif assento == "Corr":
                linha_colorida.append("⬜ Corr ")  # Branco para o corredor
            elif assento.startswith("X-"):
                linha_colorida.append("⬛ " + assento[2:] + " ")  # Cinza para assentos vendidos
            else:
                linha_colorida.append("🟩 " + assento + " ")  # Verde para assentos disponíveis
        print("".join(linha_colorida))
    print()

# Função que vende o assento solicitado, se ele estiver disponível
def vender_assento(matriz, assento):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == assento:
                matriz[i][j] = "X-" + assento  # Marca como vendido
                print(f"Assento {assento} vendido com sucesso!")
                return True
    print("Assento inválido ou indisponivel. Tente novamente.")
    return False

# Função para salvar o status final dos assentos em um arquivo .txt
def salvar_status_em_arquivo(matriz):
    try:
        with open("status_assentos.txt", "w") as arquivo:  # Abre o arquivo em modo de escrita
            for linha in matriz:
                arquivo.write(" ".join(linha) + "\n")
        print("Status dos assentos salvo em 'status_assentos.txt'.")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

# Função para carregar o status dos assentos de um arquivo .txt
def carregar_status_do_arquivo():
    try:
        with open("status_assentos.txt", "r") as arquivo:
            linhas = arquivo.readlines()
            if not linhas:  # Verifica se o arquivo está vazio
                raise FileNotFoundError
            matriz = [linha.strip().split() for linha in linhas]
        print("Status dos assentos carregado de 'status_assentos.txt'.")
        return matriz
    except FileNotFoundError:
        print("Arquivo 'status_assentos.txt' não encontrado ou vazio. Gerando nova matriz de assentos.")
        return gerar_matriz_assentos()
    except Exception as e:
        print(f"Erro ao carregar o arquivo: {e}")
        return gerar_matriz_assentos()

# Função para gerar um relatório com os assentos vendidos e disponíveis
def gerar_relatorio(matriz):
    try:
        # Contadores para assentos vendidos e disponíveis
        total_vendidos = 0
        total_disponiveis = 0

        # Abrir o arquivo para salvar o relatório
        with open("relatorio_assentos.txt", "w") as arquivo:
            arquivo.write("Relatório de Assentos - PoccoBus\n")
            arquivo.write("=" * 40 + "\n\n")

            # Escrever o status de cada linha da matriz
            for linha in matriz:
                for assento in linha:
                    if assento.startswith("X-"):  # Assento vendido
                        total_vendidos += 1
                        arquivo.write(f"{assento[2:]} - Vendido\n")
                    elif assento not in ("Mot", "Corr"):  # Assento disponível
                        total_disponiveis += 1
                        arquivo.write(f"{assento} - Disponivel\n")

            # Escrever o resumo no final do relatório
            arquivo.write("\nResumo:\n")
            arquivo.write(f"Total de assentos vendidos: {total_vendidos}\n")
            arquivo.write(f"Total de assentos disponiveis: {total_disponiveis}\n")

        print("Relatório gerado com sucesso em 'relatorio_assentos.txt'.")
    except Exception as e:
        print(f"Erro ao gerar o relatório: {e}")

# Função principal que gerencia o fluxo de vendas
def principal():
    matriz_assentos = carregar_status_do_arquivo()  # Carrega a matriz do arquivo ou gera nova

    # Extrai automaticamente os assentos disponíveis
    assentos_disponiveis = {assento for linha in matriz_assentos for assento in linha if assento not in ("Mot", "Corr") and not assento.startswith("X-")}

    while True:
        mostrar_assentos_coloridos(matriz_assentos)
        assento_escolhido = input("Digite o assento que deseja comprar (ou 'sair' para encerrar): ").upper()

        if assento_escolhido == "SAIR":
            break

        if assento_escolhido in assentos_disponiveis:
            venda_realizada = vender_assento(matriz_assentos, assento_escolhido)
            if venda_realizada:
                assentos_disponiveis.remove(assento_escolhido)
        else:
            print("Entrada inválida! Digite um assento disponível (por exemplo, A01) ou 'sair'.")

    salvar_status_em_arquivo(matriz_assentos)
    gerar_relatorio(matriz_assentos)  # Gera o relatório ao final
    print("Encerrando o sistema. Obrigado por usar a PoccoBus!")

print (principal())