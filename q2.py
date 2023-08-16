# Questão 2
# Considere que você tenha feito o web scraping de informações sobre filmes em um site de avaliações de filmes. Você obteve os seguintes dados para três filmes:
filmes = [
{"titulo": "O Senhor dos Anéis", "ano": 2001, "avaliacao": 8.8},
{"titulo": "Matrix", "ano": 1999, "avaliacao": 9.3},
{"titulo": "Interestelar", "ano": 2014, "avaliacao": 8.6}
]
# Calcule e apresente:
# ● A média das avaliações dos filmes.
# ● O título do filme com a maior avaliação.
# ● O ano de lançamento do filme com a menor avaliação.

avaliacoes = []
for filme in filmes:
    avaliacoes.append(filme["avaliacao"])

def achar_maior(dicionario, avaliacoes):
    maior_avaliacao = max(avaliacoes)
    for filme in dicionario:
        if filme["avaliacao"] == maior_avaliacao:
            return filme["titulo"]

def achar_menor(dicionario, avaliacoes):
    menor_avaliacao = min(avaliacoes)
    for filme in dicionario:
        if filme["avaliacao"] == menor_avaliacao:
            return filme["ano"]

menor_avaliacao =  min(avaliacoes)
filme_maior_avaliacao =  achar_maior(filmes, avaliacoes)
ano_menor_avaliacao = achar_menor(filmes, avaliacoes)

media_avaliacao = sum(avaliacoes)/len(avaliacoes)
print("Média da avaliação é:", media_avaliacao)
print("título do filme com a maior avaliação:", filme_maior_avaliacao)
print("O ano de lançamento do filme com a menor avaliação:", ano_menor_avaliacao)

