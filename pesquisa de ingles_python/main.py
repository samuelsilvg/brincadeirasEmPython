import funcoes

# Listando os jogos mais jogados:
arqEntrada1 = 'entradas/listaJogosJogadosOT.txt'
arqSaida1 = 'saídas/listaOrdenadaJogos.txt'
funcoes.analiseTexto(arqEntrada1, arqSaida1)

# Listando os gêneros mais jogados:
arqEntrada2 = 'entradas/listaGenerosJogadosOT.txt'
arqSaida2 = 'saídas/listaOrdenadaGenerosJogados.txt'
funcoes.analiseTexto(arqEntrada2, arqSaida2)

# Listando os gêneros mais recomendados:
arqEntrada1 = 'entradas/listaGenerosRecomendados.txt'
arqSaida1 = 'saídas/listaOrdenadaGenerosRecomendados.txt'
funcoes.analiseTexto(arqEntrada1, arqSaida1)