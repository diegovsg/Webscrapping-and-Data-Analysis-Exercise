# Questão 1
# Utilizando a biblioteca Requests BeautifulSoup, escreva um código em Python que faça o web scraping do título, up votes e do link das três primeiras postagens do subreddit r/programming no Reddit.
# O algoritmo deve guardar essas informações de forma tabular em uma planilha excel ou csv.
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd


response = requests.get(url='https://www.reddit.com/r/programming/')
soup = BeautifulSoup(response.content, features="html.parser")

dados_postagens = []
posts = soup.find_all("shreddit-post")[:3]
#print(posts)
for post in posts:
    post_tag = post.find('div', {"slot":"title"})
    title = post_tag.get_text()
    up_vote = post.get("score")
    # link = post.get("content-shef")
    post_link = post.find('a', {"slot": "full-post-link"})
    link = post_link.get('href')
    dados_postagens.append((title, up_vote, link))


#CSV file
with open('reddit_programming_posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Title', 'Up Votes', 'Link'])
    csvwriter.writerows(dados_postagens)

# Read the CSV file
df = pd.read_csv('reddit_programming_posts.csv')

# Save as Excel file
df.to_excel('reddit_programming_posts.xlsx', index=False)
