import pandas as pd
import matplotlib.pyplot as plt

#carregando dados json
data = pd.read_json('dados_compras.json')

print("------------------Exploração dos dados-----------------")
# #Verificar valores iniciais do conjunto de dados
# data.head()
# print(data.head())
# #vefiricar valores ausentes nos dados
# data.isnull().sum()
# print(data.isnull().sum())
# #Identifique a quantidade total de compras realizadas.
qtd_total_compras_realizadas = len(data)
# print(f"O total de compras realizadas foi de: {qtd_total_compras_realizadas}")

print("------------------Análise de Compras-------------------")
# Calcule a média, o valor mínimo e máximo gasto por compra
media_gasto = data['Valor'].mean()
valor_minimo = data['Valor'].min()
valor_maximo = data['Valor'].max()
# print(f"Média de gasto por compra: {media_gasto:.2f}")
# print(f"Valor mínimo gasto por compra: {valor_minimo:.2f}")
# print(f"Valor máximo gasto por compra: {valor_maximo:.2f}")
# # Determine o produto mais caro e o produto mais barato
produto_mais_caro = data[data['Valor'] == valor_maximo]["Nome do Item"].iloc[0]
produto_mais_barato = data[data['Valor'] == valor_minimo]["Nome do Item"].iloc[0]
# print(f"Produto mais caro: {produto_mais_caro}")
# print(f"Produto mais barato: {produto_mais_barato}")

print("------------------Segmentação por Gênero-------------------")
# Analise a distribuição de gênero entre os consumidores
genero_distribuicao = data['Sexo'].value_counts()
# print(genero_distribuicao)
# Calcule o valor total gasto em compras por gênero
valor_total_por_genero = data.groupby('Sexo')['Valor'].sum()
# print(valor_total_por_genero)
print("------------------Visualização de Dados-------------------")
plt.figure(figsize=(10, 6))
cores_pizza = ['#9575cd', '#b0bec5', '#3f51b5']

# Gráfico pizza para distribuição de gênero
plt.subplot(1, 2, 1)
genero_distribuicao.plot(kind='bar', color=['#8bc34a', '#03a9f4', '#e57373'])
plt.title('Quantidades de compras por gênero')
plt.xlabel('Gênero')
plt.ylabel('Quantidade')

# Gráfico de barras para valor total gasto por gênero
plt.figure(figsize=(6, 6))
valor_total_por_genero.plot(kind='pie', autopct='%1.1f%%', colors=['#9575cd', '#b0bec5', '#3f51b5'])
plt.title('Porcentagem de gasto por gênero')
plt.xlabel('Gênero')
plt.ylabel('Valor Total Gasto')

# Criar um gráfico de pizza com porcentagens e valores numéricos
plt.subplot(1, 2, 1)
valor_total_por_genero.plot(kind='pie', autopct=lambda p: '{:.1f}%\n({:.0f})'.format(p, p * sum(valor_total_por_genero) / 100), colors=cores_pizza)
plt.title('Porcentagem de gasto por gênero')
plt.ylabel('')