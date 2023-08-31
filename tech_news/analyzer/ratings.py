# Requisito 10
from collections import Counter

from tech_news.database import find_news


def top_5_categories():
    categories = find_news()
    categories_list = [category["category"] for category in categories]

    categories_dict = Counter(categories_list)

    top_5_categories = sorted(
        categories_dict.keys(),
        key=lambda category: (-categories_dict[category], category),
    )[:5]

    return top_5_categories
