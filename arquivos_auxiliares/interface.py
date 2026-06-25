"""Interface de terminal, consultas e simulações do SIGIC."""

from arquivos_auxiliares.algoritmos import (
    bfs,
    calcular_perda_energetica,
    caminho_bfs,
    dfs,
    dijkstra,
    distancia_total_caminho,
)
from arquivos_auxiliares.dados import LISTA_MODULOS, MODULOS
from arquivos_auxiliares.rede import GRAFO, MATRIZ_ADJACENCIA


def linha():
    print("-" * 72)


def pausar():
    input("\nPressione ENTER para continuar...")


def listar_modulos():
    linha()
    print("MÓDULOS DA COLÔNIA AURORA SIGER")
    linha()
    for indice, nome in enumerate(LISTA_MODULOS, start=1):
        dados = MODULOS[nome]
        print(
            f"{indice}. {nome} | prioridade {dados['prioridade']} | "
            f"consumo {dados['consumo']} kWh | status: {dados['status']}"
        )


def consultar_modulo(nome=None):
    if nome is None:
        nome = escolher_modulo("Digite o nome ou número do módulo: ")
    if nome not in MODULOS:
        print("Módulo não encontrado.")
        return

    dados = MODULOS[nome]
    linha()
    print(f"DETALHES DO MÓDULO: {nome}")
    linha()
    print(f"Descrição: {dados['descricao']}")
    print(f"Consumo energético: {dados['consumo']} kWh")
    print(f"Prioridade operacional: {dados['prioridade']}")
    print(f"Capacidade de armazenamento: {dados['capacidade']} unidades")
    print(f"Necessidade de comunicação: {dados['comunicacao']}")
    print(f"Status operacional: {dados['status']}")
    print("Conexões:")
    for conexao in GRAFO[nome]:
        print(
            f"  -> {conexao['destino']} | distância {conexao['distancia']} km | "
            f"peso {conexao['peso']}"
        )


def visualizar_rede():
    linha()
    print("REDE DA COLÔNIA - LISTA DE ADJACÊNCIA")
    linha()
    for modulo, conexoes in GRAFO.items():
        destinos = [
            f"{item['destino']} (peso {item['peso']})" for item in conexoes
        ]
        print(f"{modulo}: {', '.join(destinos)}")


def visualizar_matriz():
    linha()
    print("MATRIZ DE ADJACÊNCIA - PESOS DAS CONEXÕES")
    linha()
    abreviacoes = [nome[:4].upper() for nome in LISTA_MODULOS]
    print("      " + " ".join(f"{sigla:>6}" for sigla in abreviacoes))
    for nome, linha_matriz in zip(LISTA_MODULOS, MATRIZ_ADJACENCIA):
        valores = " ".join(f"{valor:>6}" for valor in linha_matriz)
        print(f"{nome[:4].upper():>4}: {valores}")
    print("\nLegenda:")
    for sigla, nome in zip(abreviacoes, LISTA_MODULOS):
        print(f"{sigla}: {nome}")


def executar_bfs():
    inicio = escolher_modulo("Módulo inicial para BFS: ")
    if inicio:
        ordem = bfs(inicio)
        print("\nOrdem de exploração BFS:")
        print(" -> ".join(ordem))


def executar_dfs():
    inicio = escolher_modulo("Módulo inicial para DFS: ")
    if inicio:
        ordem = dfs(inicio)
        print("\nOrdem de exploração DFS:")
        print(" -> ".join(ordem))
        if len(ordem) == len(MODULOS):
            print("Resultado: a rede está conectada a partir desse módulo.")
        else:
            print("Resultado: existem módulos isolados ou inacessíveis.")


def executar_dijkstra():
    origem = escolher_modulo("Módulo de origem: ")
    destino = escolher_modulo("Módulo de destino: ")
    if not origem or not destino:
        return
    caminho, custo = dijkstra(origem, destino)
    if not caminho:
        print("Não existe caminho entre os módulos informados.")
        return
    print("\nMelhor rota encontrada por Dijkstra:")
    print(" -> ".join(caminho))
    print(f"Custo total ponderado: {round(custo, 2)}")
    print(f"Distância física aproximada: {distancia_total_caminho(caminho)} km")


def simular_envio_energia(destino=None):
    origem = "Armazenamento de Energia"
    if destino is None:
        destino = escolher_modulo(
            "Módulo que receberá energia (ex.: Centro Medico): "
        )
    if not destino:
        return
    caminho, custo = dijkstra(origem, destino)
    if not caminho:
        print("Não foi possível enviar energia para esse módulo.")
        return

    consumo_destino = MODULOS[destino]["consumo"]
    indicadores = calcular_perda_energetica(caminho, consumo_destino)
    linha()
    print("SIMULAÇÃO DE ENVIO DE ENERGIA")
    linha()
    print(f"Origem: {origem}")
    print(f"Destino: {destino}")
    print(f"Rota recomendada: {' -> '.join(caminho)}")
    print(f"Custo ponderado da rota: {round(custo, 2)}")
    print(f"Distância total: {indicadores['distancia']} km")
    print(f"Consumo do destino: {consumo_destino} kWh")
    print(f"Perda estimada: {indicadores['perda_total']} kWh")
    print(f"Energia que deve ser enviada: {indicadores['energia_enviada']} kWh")
    print(f"Eficiência da rota: {indicadores['eficiencia']}%")


def simular_falha_operacional():
    modulo = escolher_modulo("Módulo em falha ou alerta: ")
    if not modulo:
        return

    dados = MODULOS[modulo]
    impacto = dados["prioridade"] * dados["consumo"]
    linha()
    print("SIMULAÇÃO DE FALHA OPERACIONAL")
    linha()
    print(f"Módulo analisado: {modulo}")
    print(f"Prioridade: {dados['prioridade']}")
    print(f"Consumo: {dados['consumo']} kWh")
    print(f"Indicador de impacto: {impacto}")

    if dados["prioridade"] >= 5:
        print("Ação recomendada: restauração imediata e redirecionamento de energia.")
    elif dados["prioridade"] == 4:
        print("Ação recomendada: monitoramento intensivo e redução temporária de carga.")
    else:
        print("Ação recomendada: agendar manutenção sem interromper sistemas vitais.")

    print("\nMódulos mais próximos que podem apoiar a operação:")
    conexoes_ordenadas = sorted(GRAFO[modulo], key=lambda item: item["peso"])
    for conexao in conexoes_ordenadas[:3]:
        print(f"  -> {conexao['destino']} (peso {conexao['peso']})")


def comparar_rotas_energia():
    destino = escolher_modulo("Destino para comparar eficiência energética: ")
    if not destino:
        return

    origem = "Armazenamento de Energia"
    caminho_dijkstra, _ = dijkstra(origem, destino)
    rota_exploratoria = caminho_bfs(origem, destino)

    linha()
    print("COMPARAÇÃO DE ROTAS")
    linha()
    if caminho_dijkstra:
        indicador = calcular_perda_energetica(
            caminho_dijkstra, MODULOS[destino]["consumo"]
        )
        print("Rota otimizada por Dijkstra:")
        print(f"  {' -> '.join(caminho_dijkstra)}")
        print(
            f"  Perda: {indicador['perda_total']} kWh | "
            f"Eficiência: {indicador['eficiencia']}%"
        )

    if rota_exploratoria and rota_exploratoria[-1] == destino:
        indicador = calcular_perda_energetica(
            rota_exploratoria, MODULOS[destino]["consumo"]
        )
        print("\nRota exploratória com menor número de conexões por BFS:")
        print(f"  {' -> '.join(rota_exploratoria)}")
        print(
            f"  Perda: {indicador['perda_total']} kWh | "
            f"Eficiência: {indicador['eficiencia']}%"
        )
    else:
        print("\nNão foi possível montar uma rota exploratória simples por BFS.")


def exibir_modelagem_matematica():
    linha()
    print("MODELAGEM MATEMÁTICA - EFICIÊNCIA ENERGÉTICA")
    linha()
    print("Fórmula de perda:")
    print("  perda_total = distancia_total * taxa_perda * consumo_destino")
    print("Fórmula de eficiência:")
    print("  eficiencia = energia_recebida / energia_enviada")
    print("\nVariáveis:")
    print("  distancia_total: soma das distâncias da rota em km")
    print("  taxa_perda: perda estimada por km de conexão")
    print("  consumo_destino: energia necessária para o módulo funcionar")
    print("  energia_recebida: energia útil que chega ao módulo")
    print("  energia_enviada: consumo do módulo somado às perdas da rota")
    print(
        "\nAnálise: rotas mais longas aumentam a perda energética. "
        "Assim, o Dijkstra ajuda a reduzir desperdício ao escolher rotas "
        "com menor custo ponderado."
    )


def exibir_sustentabilidade_governanca():
    linha()
    print("SUSTENTABILIDADE E GOVERNANÇA")
    linha()
    print("- Priorizar energia para suporte médico, oxigênio, controle e habitação.")
    print("- Usar rotas de menor perda para reduzir desperdício energético.")
    print("- Monitorar módulos em alerta antes que causem falhas em cadeia.")
    print("- Planejar novas conexões evitando sobrecarga em um único módulo.")
    print("- Registrar critérios de decisão para uma governança tecnológica clara.")
    print("- Balancear consumo, comunicação e prioridade operacional da colônia.")


def identificar_modulos_criticos():
    linha()
    print("MÓDULOS CRÍTICOS POR PRIORIDADE E CONSUMO")
    linha()
    ordenados = sorted(
        MODULOS.items(),
        key=lambda item: (item[1]["prioridade"], item[1]["consumo"]),
        reverse=True,
    )
    for nome, dados in ordenados:
        indicador = dados["prioridade"] * dados["consumo"]
        print(
            f"{nome}: prioridade {dados['prioridade']}, consumo "
            f"{dados['consumo']} kWh, indicador {indicador}"
        )


def escolher_modulo(mensagem):
    listar_modulos()
    valor = input(f"\n{mensagem}").strip()
    if valor.isdigit():
        indice = int(valor) - 1
        if 0 <= indice < len(LISTA_MODULOS):
            return LISTA_MODULOS[indice]
    for modulo in LISTA_MODULOS:
        if modulo.lower() == valor.lower():
            return modulo
    print("Opção inválida.")
    return None


def demonstracao_automatica():
    linha()
    print("DEMONSTRAÇÃO AUTOMÁTICA DO SIGIC")
    linha()
    listar_modulos()
    print("\nExemplo BFS a partir do Centro de Controle:")
    print(" -> ".join(bfs("Centro de Controle")))
    print("\nExemplo DFS a partir do Centro de Controle:")
    print(" -> ".join(dfs("Centro de Controle")))
    print("\nExemplo Dijkstra: Armazenamento de Energia até Centro Medico")
    caminho, custo = dijkstra("Armazenamento de Energia", "Centro Medico")
    print(" -> ".join(caminho))
    print(f"Custo ponderado: {round(custo, 2)}")
    print()
    simular_envio_energia("Centro Medico")


def exibir_menu():
    linha()
    print("SIGIC - AURORA SIGER")
    linha()
    print("1. Visualizar módulos")
    print("2. Consultar módulo")
    print("3. Visualizar rede da colônia")
    print("4. Visualizar matriz de adjacência")
    print("5. Executar BFS")
    print("6. Executar DFS")
    print("7. Executar Dijkstra")
    print("8. Simular envio de energia")
    print("9. Simular falha operacional")
    print("10. Comparar rotas de energia")
    print("11. Exibir modelagem matemática")
    print("12. Exibir sustentabilidade e governança")
    print("13. Identificar módulos críticos")
    print("14. Demonstração automática")
    print("0. Sair")
