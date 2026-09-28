print("=== PESQUISA DE OPINIÃO - TUDOWEB ===")
print("Avaliação do atendimento ao cliente")
print()

# Contadores das respostas
qtd_excelente = 0
qtd_ruim = 0

# Versão de teste solicitada na atividade
total_entrevistados = 10

for numero in range(1, total_entrevistados + 1):
    print(f"\n--- Entrevistado {numero} de {total_entrevistados} ---")

    nome = input("Digite o nome do entrevistado: ")
    idade = input("Digite a idade do entrevistado: ")

    # Validação da opinião
    while True:
        print("\nComo você avalia o atendimento?")
        print("1 - EXCELENTE")
        print("2 - BOM")
        print("3 - RUIM")

        opiniao = input("Digite a opção desejada (1, 2 ou 3): ")

        if opiniao == "1":
            qtd_excelente += 1
            avaliacao = "EXCELENTE"
            break

        elif opiniao == "2":
            avaliacao = "BOM"
            break

        elif opiniao == "3":
            qtd_ruim += 1
            avaliacao = "RUIM"
            break

        else:
            print("Opção inválida! Digite somente 1, 2 ou 3.")

    print(f"\nResposta registrada: {nome}, {idade} anos - {avaliacao}")

print("\n===================================")
print("RESULTADO FINAL DA PESQUISA")
print("===================================")
print(f'Quantidade de respostas "EXCELENTE": {qtd_excelente}')
print(f'Quantidade de respostas "RUIM": {qtd_ruim}')
print("===================================")
print("Pesquisa finalizada com sucesso!")
