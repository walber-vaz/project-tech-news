from datetime import datetime

from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    """
    Search news by title.

    Args:
        title (str): The title to search for.

    Returns:
        list: A list of tuples containing the title and URL of matching news.
    """
    search = search_news({"title": {"$regex": title, "$options": "i"}})
    list_news = [(news["title"], news["url"]) for news in search]
    return list_news


# Requisito 8
def search_by_date(date):
    """
    Search news articles by date.

    Args:
        date (str): The date to search for news articles in the format
        "YYYY-MM-DD".

    Returns:
        list: A list of tuples containing the title and URL of the news
        articles found.

    Raises:
        ValueError: If the input date is invalid.

    Example:
        >>> search_by_date("2022-01-15")
        [("News Article 1", "https://news-article-1.com"),
         ("News Article 2", "https://news-article-2.com")]
    """
    try:
        date_format = datetime.strptime(date, "%Y-%m-%d")
        date_new_format = date_format.strftime("%d/%m/%Y")
        search = search_news({"timestamp": {"$regex": date_new_format}})
        list_news = [(news["title"], news["url"]) for news in search]
        return list_news
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    """
    Searches for news articles based on a given category.

    Args:
        category (str): The category to search for.

    Returns:
        list: A list of tuples containing the title and URL of
        the news articles found.
    """
    search = search_news({"category": {"$regex": category, "$options": "i"}})
    list_news = [(news["title"], news["url"]) for news in search]
    return list_news
