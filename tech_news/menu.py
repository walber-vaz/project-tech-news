import sys

from tech_news.analyzer.ratings import top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_category,
    search_by_date,
    search_by_title,
)
from tech_news.scraper import get_tech_news


def handle_action_0():
    """
    Prompt the user to enter the quantity of news to be searched.
    Convert the input to an integer and assign it to the 'quantity' variable.
    Call the 'get_tech_news' function with the 'quantity' as an argument.
    Return the result of the 'get_tech_news' function.
    """
    quantity = int(input("Digite quantas notícias serão buscadas:"))

    return get_tech_news(quantity)


def handle_action_1():
    """
    A function that handles action 1.

    This function prompts the user to enter a title and then calls the
    'search_by_title' function with the inputted title as an argument.
    It returns the result of the 'search_by_title' function.

    Parameters:
        None

    Returns:
        The result of the 'search_by_title' function.
    """
    title = input("Digite o título:")

    return search_by_title(title)


def handle_action_2():
    """
    Handle action 2.

    Prompts the user to input a date in the format 'yyyy-mm-dd',
    and then calls the 'search_by_date' function
    with the inputted date as a parameter.

    Parameters:
    None

    Returns:
    The result of the 'search_by_date' function call.
    """
    date = input("Digite a data no formato aaaa-mm-dd:")

    return search_by_date(date)


def handle_action_3():
    """
    A function that handles action 3.

    This function prompts the user to input a category and then calls the
    search_by_category function with the provided category as an argument.

    Returns:
        The result of the search_by_category function call.
    """
    category = input("Digite a categoria:")

    return search_by_category(category)


def handle_action_4():
    """
    Generate a function comment for the given function body in a markdown
    code block with the correct language syntax.

    :return: A string containing the function comment.
    :rtype: str
    """
    return top_5_categories()


def handle_action_5():
    """
    Handle action 5 and print a message.

    This function takes no parameters and returns None.

    Returns:
        None: If the action is handled successfully.

    Examples:
        >>> handle_action_5()
        Encerrando script

    """
    return print("Encerrando script\n")


# Requisito 12
def analyzer_menu():
    """
    Displays a menu to the user and performs the corresponding action based
    on the selected option.

    Parameters:
    - None

    Returns:
    - None

    Raises:
    - None
    """
    option = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por categoria;\n"
        " 4 - Listar top 5 categorias;\n"
        " 5 - Sair."
    )

    menu_actions = {
        "0": handle_action_0,
        "1": handle_action_1,
        "2": handle_action_2,
        "3": handle_action_3,
        "4": handle_action_4,
        "5": handle_action_5,
    }

    try:
        return menu_actions[option]()  # type: ignore

    except Exception:
        return print("Opção inválida", file=sys.stderr)
