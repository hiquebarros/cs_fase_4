"""Algoritmos de grafos e modelagem energética do SIGIC."""

from heapq import heappop, heappush

from arquivos_auxiliares.dados import MODULOS
from arquivos_auxiliares.rede import GRAFO


def bfs(inicio):
    visitados = set()
    fila = [inicio]
    ordem = []

    while fila:
        atual = fila.pop(0)
        if atual not in visitados:
            visitados.add(atual)
            ordem.append(atual)
            for conexao in GRAFO[atual]:
                destino = conexao["destino"]
                if destino not in visitados and destino not in fila:
                    fila.append(destino)
    return ordem


def caminho_bfs(origem, destino):
    visitados = {origem}
    fila = [(origem, [origem])]

    while fila:
        atual, caminho = fila.pop(0)
        if atual == destino:
            return caminho
        for conexao in GRAFO[atual]:
            proximo = conexao["destino"]
            if proximo not in visitados:
                visitados.add(proximo)
                fila.append((proximo, caminho + [proximo]))
    return []


def dfs(inicio):
    visitados = set()
    ordem = []

    def visitar(modulo):
        visitados.add(modulo)
        ordem.append(modulo)
        for conexao in GRAFO[modulo]:
            destino = conexao["destino"]
            if destino not in visitados:
                visitar(destino)

    visitar(inicio)
    return ordem


def dijkstra(origem, destino):
    distancias = {modulo: float("inf") for modulo in MODULOS}
    anteriores = {modulo: None for modulo in MODULOS}
    distancias[origem] = 0
    fila_prioridade = [(0, origem)]

    while fila_prioridade:
        distancia_atual, atual = heappop(fila_prioridade)
        if atual == destino:
            break
        if distancia_atual > distancias[atual]:
            continue

        for conexao in GRAFO[atual]:
            vizinho = conexao["destino"]
            nova_distancia = distancia_atual + conexao["peso"]
            if nova_distancia < distancias[vizinho]:
                distancias[vizinho] = nova_distancia
                anteriores[vizinho] = atual
                heappush(fila_prioridade, (nova_distancia, vizinho))

    caminho = reconstruir_caminho(anteriores, origem, destino)
    return caminho, distancias[destino]


def reconstruir_caminho(anteriores, origem, destino):
    caminho = []
    atual = destino
    while atual is not None:
        caminho.insert(0, atual)
        atual = anteriores[atual]
    if caminho and caminho[0] == origem:
        return caminho
    return []


def distancia_total_caminho(caminho):
    distancia_total = 0
    for origem, destino in zip(caminho, caminho[1:]):
        for conexao in GRAFO[origem]:
            if conexao["destino"] == destino:
                distancia_total += conexao["distancia"]
                break
    return round(distancia_total, 2)


def calcular_perda_energetica(caminho, consumo_destino, taxa_perda=0.015):
    distancia = distancia_total_caminho(caminho)
    perda_total = distancia * taxa_perda * consumo_destino
    energia_enviada = consumo_destino + perda_total
    eficiencia = consumo_destino / energia_enviada if energia_enviada else 0
    return {
        "distancia": round(distancia, 2),
        "perda_total": round(perda_total, 2),
        "energia_enviada": round(energia_enviada, 2),
        "energia_recebida": consumo_destino,
        "eficiencia": round(eficiencia * 100, 2),
        "taxa_perda": taxa_perda,
    }
