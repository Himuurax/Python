secreto = 'fruta'
digitados = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu!!!')
        break

    letra = input('Digite um letra: ')

    len(letra) >= 1

    if len(letra) > 1:
        print('Ahh isso não vale, digite apenas uma letra.')
        continue

    digitados.append(letra)

    if letra in secreto:
        print(f'UHUUL, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'Affz a letra "{letra}" NÃO existe na palavra secreta.')
        digitados.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:

        if letra_secreta in digitados:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'

    if secreto_temporario == secreto:
        print('Que legal, VOCÊ GANHOU !!!')
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')

    if letra not in secreto:
        chances = chances - 1

    print(f'Você ainda tem {chances} chances.')
    print()
