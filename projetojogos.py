"""
Meus Jogos Favoritos
Sistema de gerenciamento
Criado por Julia Baptista
"""

from time import sleep
import json

ARQUIVO = 'jogos.json'
jogos = []


def carregar_jogos():
    global jogos
    try:
        arquivo = open(ARQUIVO, 'r', encoding='utf-8') # Abre em modo leitura
        jogos = json.load(arquivo) # Converte o JSON em lista Python
        arquivo.close()

    except FileNotFoundError:
        jogos = []


def salvar_jogos():
    arquivo = open(ARQUIVO, 'w', encoding='utf-8') # Apaga o conteúdo antigo reescreve
    json.dump(jogos, arquivo, indent=4, ensure_ascii=False)
    arquivo.close()


def adicionar_jogo():
    print('\n🎯 ADICIONAR NOVO JOGO')

    nome = input('\nNome do jogo: ')
    plataforma = input('Plataforma: ')
    status = input('Status (Jogando / Zerado / Wishlist): ').capitalize()
    horas = int(input('Horas jogadas: '))
    nota = float(input('Nota (0 a 10): '))

    jogo = {
        'nome': nome,
        'plataforma': plataforma,
        'status': status,
        'horas': horas,
        'nota': nota
    }

    jogos.append(jogo)
    salvar_jogos()

    print('\n✅ Jogo adicionado com sucesso!')


def listar_jogos():
    print('\n📜 LISTA DE JOGOS')

    if len(jogos) == 0:
        print('\nNenhum jogo cadastrado ainda.')
        return

    for i, jogo in enumerate(jogos, start=1):
        print(f'\n🎮 Jogo {i}')
        print(f"Nome: {jogo['nome']}")
        print(f"Plataforma: {jogo['plataforma']}")
        print(f"Status: {jogo['status']}")
        print(f"Horas jogadas: {jogo['horas']}")
        print(f"Nota: {jogo['nota']}")


def editar_jogo():
    print('\n✏️  EDITAR JOGO')

    if len(jogos) == 0:
        print('\nNão há jogos para editar.')
        return

    listar_jogos()

    try:
        escolha = int(input('\nDigite o número do jogo: '))

        if 1 <= escolha <= len(jogos):
            jogo = jogos[escolha - 1]

            print('\nPressione ENTER para manter o valor atual')

            nome = input(f"\nNome ({jogo['nome']}): ") or jogo['nome']
            plataforma = input(f"Plataforma ({jogo['plataforma']}): ") or jogo['plataforma']
            status = input(f"Status ({jogo['status']}): ") or jogo['status']

            horas = input(f"Horas ({jogo['horas']}): ")
            horas = int(horas) if horas else jogo['horas']

            nota = input(f"Nota ({jogo['nota']}): ")
            nota = float(nota) if nota else jogo['nota']

            jogo.update({
                'nome': nome,
                'plataforma': plataforma,
                'status': status,
                'horas': horas,
                'nota': nota
            })

            salvar_jogos()
            print('\n✅ Jogo atualizado com sucesso!')

        else:
            print('\n❌ Número inválido.')

    except ValueError:
        print('\n❌ Digite um número válido.')


def apagar_jogo():
    print('\n🗑️  APAGAR JOGO')

    if len(jogos) == 0:
        print('\nNão há jogos para apagar.')
        return

    listar_jogos()

    try:
        escolha = int(input('\nDigite o número do jogo: '))

        if 1 <= escolha <= len(jogos):
            removido = jogos.pop(escolha - 1)
            salvar_jogos()
            print(f"\n✅ '{removido['nome']}' removido!")

        else:
            print('\n❌ Número inválido.')

    except ValueError:
        print('\n❌ Digite um número válido.')


def menu():
    carregar_jogos()

    while True:
        print('\n===== GERENCIADOR DE JOGOS =====')
        sleep(1)
        print('\n1 - Adicionar novo jogo')
        print('2 - Ver jogos cadastrados')
        print('3 - Editar jogo')
        print('4 - Apagar jogo')
        print('5 - Sair')

        opcao = input('\nEscolha: ')

        if opcao == '1':
            adicionar_jogo()

        elif opcao == '2':
            listar_jogos()

        elif opcao == '3':
            editar_jogo()

        elif opcao == '4':
            apagar_jogo()

        elif opcao == '5':
            print('\n👋 Saindo...')
            sleep(1)
            print('\nAté breve!')
            print()
            salvar_jogos()
            break

        else:
            print('\n❌ Opção inválida!')


menu()
