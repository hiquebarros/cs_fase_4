"""Dados operacionais da colônia Aurora Siger."""


# Dicionário principal de módulos da colônia.
MODULOS = {
    "Habitacao": {
        "consumo": 180,
        "prioridade": 5,
        "capacidade": 120,
        "comunicacao": "alta",
        "status": "ativo",
        "descricao": "Acomoda a tripulação e oferece suporte básico de sobrevivência.",
    },
    "Centro de Controle": {
        "consumo": 220,
        "prioridade": 5,
        "capacidade": 80,
        "comunicacao": "critica",
        "status": "ativo",
        "descricao": "Monitora e coordena as operações da Aurora Siger.",
    },
    "Armazenamento de Energia": {
        "consumo": 90,
        "prioridade": 5,
        "capacidade": 900,
        "comunicacao": "media",
        "status": "ativo",
        "descricao": "Armazena a energia produzida e abastece os demais módulos.",
    },
    "Agricultura": {
        "consumo": 260,
        "prioridade": 4,
        "capacidade": 300,
        "comunicacao": "media",
        "status": "ativo",
        "descricao": "Produz alimentos e contribui com a sustentabilidade da base.",
    },
    "Laboratorio Cientifico": {
        "consumo": 170,
        "prioridade": 3,
        "capacidade": 100,
        "comunicacao": "alta",
        "status": "ativo",
        "descricao": "Realiza pesquisas sobre materiais e condições marcianas.",
    },
    "Comunicacao": {
        "consumo": 200,
        "prioridade": 5,
        "capacidade": 70,
        "comunicacao": "critica",
        "status": "ativo",
        "descricao": "Mantém a troca de dados entre os módulos e o contato com a Terra.",
    },
    "Centro Medico": {
        "consumo": 160,
        "prioridade": 5,
        "capacidade": 90,
        "comunicacao": "alta",
        "status": "ativo",
        "descricao": "Atende emergências e monitora a saúde da tripulação.",
    },
    "Producao de Oxigenio": {
        "consumo": 240,
        "prioridade": 5,
        "capacidade": 260,
        "comunicacao": "alta",
        "status": "ativo",
        "descricao": "Gera e distribui oxigênio para a colônia.",
    },
    "Processamento de Recursos": {
        "consumo": 300,
        "prioridade": 4,
        "capacidade": 350,
        "comunicacao": "media",
        "status": "alerta",
        "descricao": "Processa água, minerais e insumos extraídos em Marte.",
    },
    "Laboratorio Atmosferico": {
        "consumo": 150,
        "prioridade": 3,
        "capacidade": 110,
        "comunicacao": "media",
        "status": "manutencao",
        "descricao": "Analisa a atmosfera marciana e apoia a produção de oxigênio.",
    },
}


# Tuplas com origem, destino, distância em km, custo energético e latência.
CONEXOES = [
    ("Armazenamento de Energia", "Centro de Controle", 2.0, 12, 4),
    ("Armazenamento de Energia", "Habitacao", 2.5, 16, 5),
    ("Armazenamento de Energia", "Agricultura", 3.0, 18, 7),
    ("Armazenamento de Energia", "Producao de Oxigenio", 2.2, 15, 5),
    ("Centro de Controle", "Comunicacao", 1.0, 8, 2),
    ("Centro de Controle", "Laboratorio Cientifico", 2.8, 14, 6),
    ("Centro de Controle", "Centro Medico", 2.4, 13, 5),
    ("Habitacao", "Centro Medico", 1.2, 7, 3),
    ("Habitacao", "Agricultura", 2.7, 15, 6),
    ("Agricultura", "Producao de Oxigenio", 1.8, 10, 4),
    ("Producao de Oxigenio", "Laboratorio Atmosferico", 1.5, 9, 3),
    ("Laboratorio Atmosferico", "Processamento de Recursos", 2.6, 17, 7),
    ("Processamento de Recursos", "Agricultura", 2.1, 14, 5),
    ("Processamento de Recursos", "Laboratorio Cientifico", 3.1, 19, 8),
    ("Laboratorio Cientifico", "Comunicacao", 1.9, 11, 4),
    ("Comunicacao", "Centro Medico", 2.3, 12, 4),
]


LISTA_MODULOS = list(MODULOS.keys())
