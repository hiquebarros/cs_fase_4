"""Construção da rede computacional da colônia."""

from arquivos_auxiliares.dados import CONEXOES, LISTA_MODULOS, MODULOS


def calcular_peso(distancia, custo_energetico, latencia):
    """Combina distância, custo energético e latência em um único peso."""
    return round((distancia * 2) + custo_energetico + (latencia * 0.5), 2)


def construir_grafo():
    grafo = {modulo: [] for modulo in MODULOS}
    for origem, destino, distancia, custo_energetico, latencia in CONEXOES:
        peso = calcular_peso(distancia, custo_energetico, latencia)
        dados = {
            "destino": destino,
            "distancia": distancia,
            "custo_energetico": custo_energetico,
            "latencia": latencia,
            "peso": peso,
        }
        dados_inversos = dados.copy()
        dados_inversos["destino"] = origem
        grafo[origem].append(dados)
        grafo[destino].append(dados_inversos)
    return grafo


def construir_matriz_adjacencia():
    tamanho = len(LISTA_MODULOS)
    indices = {modulo: indice for indice, modulo in enumerate(LISTA_MODULOS)}
    matriz = [[0 for _ in range(tamanho)] for _ in range(tamanho)]
    for origem, destino, distancia, custo_energetico, latencia in CONEXOES:
        peso = calcular_peso(distancia, custo_energetico, latencia)
        i = indices[origem]
        j = indices[destino]
        matriz[i][j] = peso
        matriz[j][i] = peso
    return matriz


GRAFO = construir_grafo()
MATRIZ_ADJACENCIA = construir_matriz_adjacencia()
