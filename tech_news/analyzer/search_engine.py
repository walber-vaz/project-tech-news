from datetime import datetime

from tech_news.database import search_news


# Requisito 7
def search_by_title(title):
    search = search_news({"title": {"$regex": title, "$options": "i"}})
    list_news = [(news["title"], news["url"]) for news in search]
    return list_news


# Requisito 8
def search_by_date(date):
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
    search = search_news({"category": {"$regex": category, "$options": "i"}})
    list_news = [(news["title"], news["url"]) for news in search]
    return list_news
