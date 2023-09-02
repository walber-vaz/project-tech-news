# Este é o arquivo de funções de acesso ao banco de dados. Basta importar e
# chamar as funçoes
# Atenção: este arquivo não deve ser alterado. Mudanças aqui não serão
# refletidas no avaliador automático.

import copy

from decouple import config
from pymongo import MongoClient

DB_HOST = config("DB_HOST", default="localhost")
DB_PORT = config("DB_PORT", default="27017")

client = MongoClient(host=DB_HOST, port=int(DB_PORT))
db = client.tech_news


def create_news(data):
    """
    This function creates news by inserting many copies of the given data
    into the news collection in the database.

    Parameters:
    - data: A list of dictionaries representing the news data to be inserted.

    Return:
    - None
    """
    db.news.insert_many(copy.deepcopy(data))


def insert_or_update(notice):
    """
    Inserts or updates a notice in the database.

    Parameters:
        notice (dict): A dictionary representing the notice to be inserted
        or updated.

    Returns:
        bool: True if the notice was inserted, False otherwise.
    """
    return (
        db.news.update_one(
            {"url": notice["url"]}, {"$set": notice}, upsert=True
        ).upserted_id
        is not None
    )


def find_news():
    """
    Retrieves a list of news articles from the database.

    Returns:
        list: A list of news articles, where each article is a dictionary
        with the keys and values representing the article's attributes.
    """
    return list(db.news.find({}, {"_id": False}))


def search_news(query):
    """
    Retrieve news articles from the database based on a given query.

    Args:
        query (dict): A dictionary specifying the search criteria.

    Returns:
        list: A list of news articles matching the query.
    """
    return list(db.news.find(query))


def get_collection():
    """
    Gets the collection of news from the database.

    Returns:
        The collection of news.
    """
    return db.news
