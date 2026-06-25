"""Arquivo principal de execução do SIGIC."""

from arquivos_auxiliares.interface import (
    comparar_rotas_energia,
    consultar_modulo,
    demonstracao_automatica,
    executar_bfs,
    executar_dfs,
    executar_dijkstra,
    exibir_menu,
    exibir_modelagem_matematica,
    exibir_sustentabilidade_governanca,
    identificar_modulos_criticos,
    listar_modulos,
    pausar,
    simular_envio_energia,
    simular_falha_operacional,
    visualizar_matriz,
    visualizar_rede,
)


def main():
    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            listar_modulos()
        elif opcao == "2":
            consultar_modulo()
        elif opcao == "3":
            visualizar_rede()
        elif opcao == "4":
            visualizar_matriz()
        elif opcao == "5":
            executar_bfs()
        elif opcao == "6":
            executar_dfs()
        elif opcao == "7":
            executar_dijkstra()
        elif opcao == "8":
            simular_envio_energia()
        elif opcao == "9":
            simular_falha_operacional()
        elif opcao == "10":
            comparar_rotas_energia()
        elif opcao == "11":
            exibir_modelagem_matematica()
        elif opcao == "12":
            exibir_sustentabilidade_governanca()
        elif opcao == "13":
            identificar_modulos_criticos()
        elif opcao == "14":
            demonstracao_automatica()
        elif opcao == "0":
            print("Encerrando o SIGIC. Missão Aurora Siger monitorada.")
            break
        else:
            print("Opção inválida. Tente novamente.")

        pausar()


if __name__ == "__main__":
    main()
