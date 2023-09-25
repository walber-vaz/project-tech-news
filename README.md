# Projeto tech news

## Objetivo

O objetivo deste projeto é criar um crawler para o site [Trybe](https://www.betrybe.com/blog/), que é uma escola de programação, e extrair as informações dos artigos de tecnologia, como título, autor, data de publicação e conteúdo. Após a extração, os dados serão salvos no banco de dados MongoDB.

## Tecnologias utilizadas

- Python
- MongoDB
- Parsel
- Requests
- Docker
- Pytest

## Requisitos do Projeto

***1 - Crie a função fetch***

---

Esta função é responsável por fazer uma requisição HTTP para o site [Trybe](https://www.betrybe.com/blog/) e retornar o conteúdo HTML da página.

***2 - Crie a função scrape_updates***

---

Esta função dev retorna uma lista de paginas de atualizações do site [Trybe](https://www.betrybe.com/blog/).

***3 - Crie a função scrape_next_page_link***

---

Esta função deve retornar a URL da próxima página de atualizações do site [Trybe](https://www.betrybe.com/blog/).

***4 - Crie a função scrape_news***

---

Essa função deve receber o conteúdo HTML de uma página de notícia e retornar um dicionário com os seguintes atributos:

- url - link para acesso da notícia.
- title - título da notícia.
- timestamp - data da notícia, no formato dd/mm/AAAA.
- writer - nome da pessoa autora da notícia.
- reading_time - número de minutos necessários para leitura.
- summary - o primeiro parágrafo da notícia.
- category - categoria da notícia.

***5 - Crie a função get_tech_news para obter as notícias***

---

Essa função deve receber como parâmetro um número inteiro n e buscar as últimas n notícias do site.

Utilize as funções fetch, scrape_updates, scrape_next_page_link e scrape_news para buscar as notícias e processar seu conteúdo.

As notícias buscadas devem ser inseridas no MongoDB; Para acessar o banco de dados, importe e utilize as funções que já temos prontas em tech_news/database.py

Após inserir as notícias no banco, a função deve retornar estas mesmas notícias.

***6 - Teste a classe ReadingPlanService***

---

A classe ReadingPlanService é responsável por gerar um plano de leitura com base nas notícias salvas no banco de dados.

***7 - Crie a função search_by_title***

---

Essa função deve receber uma string com o título da notícia e retornar uma lista com todas as notícias que possuem o título pesquisado.

***8 - Crie a função search_by_date***

---

Essa função deve receber uma string com a data da notícia no formato dd-mm-aaaa e retornar uma lista com todas as notícias que possuem a data pesquisada.

***9 - Crie a função search_by_category***

---

Essa função deve receber uma string com a categoria da notícia e retornar uma lista com todas as notícias que possuem a categoria pesquisada.

***10 - Crie a função top_5_categories***

---

Essa função deve retornar uma lista com as 5 categorias que possuem mais notícias.

## Autor

- [Walber Vaz](https://linkedin.com/in/walber-vaz)
