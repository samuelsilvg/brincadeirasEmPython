import random

with open('personagens.txt', 'r') as entrada:
    personagens = entrada.read()
    personagens = personagens.split(',')
    personagens = [personagem.strip() for personagem in personagens if personagem.strip()]

tresPersonagens = random.sample(personagens, 3)

with open('saida.txt', 'w') as saida:
    for personagem in tresPersonagens:
        saida.write(personagem + '\n')
