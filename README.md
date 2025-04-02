<h1 align="center"> Criando um método para vendas de assentos em um ônibus de viagem </h1><br/>


<p align="center"><img src="http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge"/></p>
*1. Função gerar_matriz_assentos*<br/>
Objetivo: Criar uma matriz que representa os assentos de um ônibus.<br/>
Como funciona:<br/>
A primeira linha tem o motorista ("Mot") e corredores ("Corr").<br/>
As próximas 12 linhas têm 5 colunas cada, com corredores no meio e assentos numerados (A01, A02, etc.).<br/>

*2. Função mostrar_assentos_coloridos*<br/>
Objetivo: Mostrar a matriz de assentos com emojis coloridos.<br/>
Como funciona:<br/>
Exibe uma legenda explicando os emojis.<br/>
Percorre a matriz e substitui os códigos dos assentos por emojis coloridos:<br/>
🟦 para o motorista.<br/>
⬜ para corredores.<br/>
🟩 para assentos disponíveis.<br/>
⬛ para assentos vendidos.<br/>

*3. Função vender_assento*<br/>
Objetivo: Marcar um assento como vendido.<br/>
Como funciona:<br/>
Procura o assento na matriz.<br/>
Se encontrar, marca como vendido (prefixo "X-") e retorna sucesso.<br/>
Se não encontrar, informa que o assento é inválido ou indisponível.<br/>

*4. Função salvar_status_em_arquivo*<br/>
Objetivo: Salvar o status atual dos assentos em um arquivo de texto.<br/>
Como funciona:<br/>
Abre um arquivo chamado "status_assentos.txt".<br/>
Escreve cada linha da matriz no arquivo.<br/>

*5. Função carregar_status_do_arquivo*<br/>
Objetivo: Carregar o status dos assentos de um arquivo de texto.<br/>
Como funciona:<br/>
Tenta abrir e ler o arquivo "status_assentos.txt".<br/>
Se o arquivo não existir ou estiver vazio, gera uma nova matriz de assentos.<br/>
Se houver erro, gera uma nova matriz de assentos.<br/>

*6. Função gerar_relatorio*<br/>
Objetivo: Gerar um relatório dos assentos vendidos e disponíveis.<br/>
Como funciona:<br/>
Conta os assentos vendidos e disponíveis.<br/>
Escreve um relatório detalhado em "relatorio_assentos.txt".<br/>

*7. Função principal*<br/>
Objetivo: Gerenciar o fluxo de vendas de assentos.<br/>
Como funciona:<br/>
Carrega a matriz de assentos do arquivo ou gera uma nova.<br/>
Mostra os assentos coloridos.<br/>
Permite ao usuário comprar assentos até digitar "sair".<br/>
Salva o status final dos assentos e gera um relatório.<br/>

*8. Execução do programa*<br/>
Objetivo: Iniciar o programa.<br/>
Como funciona:<br/>
Chama a função principal para começar o processo.<br/>
