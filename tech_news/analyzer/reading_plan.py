from typing import Any, Dict, List

from tech_news.database import find_news


class ReadingPlanService:
    @staticmethod
    def _db_news_proxy():
        """
        Esse proxy existe para que seja possível mockar
        a função `find_news` do módulo `tech_news.database`
        sem afetar o teste do requisito.
        """
        return find_news()

    @classmethod
    def group_news_for_available_time(
        cls, available_time: int
    ) -> Dict[str, List]:
        """
        Group news articles based on the available time.

        This class method takes an integer `available_time` as input and
        returns a dictionary containing two lists: "readable" and "unreadable".
        The function loops through all the news articles in the database and
        checks if the reading time of each article is greater than the
        available time. If it is, the article is added to the "unreadable"
        list. If not, the function checks if the article can be fit into
        an existing group in the result dictionary. If it can, the article
        is added to the corresponding group. If not, a new group is created
        and the article is added to the "readable" list.

        Parameters:
        - `available_time` (int): The maximum available time in minutes
        for reading news articles.

        Returns:
        - result (Dict[str, List]): A dictionary containing two lists:
        "readable" and "unreadable". The "readable" list contains news
        articles that can be read within the available time, while the
        "unreadable" list contains articles that require more time to read.

        Raises:
        - ValueError: If `available_time` is less than or equal to zero.
        """
        if available_time <= 0:
            raise ValueError("Valor 'available_time' deve ser maior que zero")

        result = {"readable": [], "unreadable": []}
        for new in cls._db_news_proxy():
            if new["reading_time"] > available_time:
                cls._register_unreadable(result, new)
                continue

            if cls._fit_to_existing_group(result, new):
                continue

            cls._register_readable(available_time, result, new)
        return result

    @classmethod
    def _register_readable(
        cls, available_time: int, result: Dict[str, List], new: Dict[str, Any]
    ):
        """
        Registers a new readable item in the result dictionary.

        :param available_time: The available time in minutes.
        :type available_time: int
        :param result: The result dictionary.
        :type result: Dict[str, List]
        :param new: The new item to register.
        :type new: Dict[str, Any]
        """
        result["readable"].append(
            {
                "unfilled_time": available_time - new["reading_time"],
                "chosen_news": [(new["title"], new["reading_time"])],
            }
        )

    @classmethod
    def _register_unreadable(
        cls, result: Dict[str, List], new: Dict[str, Any]
    ):
        """
        Adds a new unreadable item to the result dictionary.

        Parameters:
            result (Dict[str, List]): The result dictionary to add
            the unreadable item to.
            new (Dict[str, Any]): The new item to be added, containing
            the title and reading time.

        Returns:
            None
        """
        result["unreadable"].append((new["title"], new["reading_time"]))

    @classmethod
    def _fit_to_existing_group(
        cls, result: Dict[str, List], new: Dict[str, Any]
    ):
        """
        Fits a new item to an existing group in the result dictionary.

        Parameters:
            result (Dict[str, List]): The result dictionary containing groups.
            new (Dict[str, Any]): The new item to fit into an existing group.

        Returns:
            bool: True if the item was successfully fit into a group,
            False otherwise.
        """
        for group in result["readable"]:
            if new["reading_time"] >= group["unfilled_time"]:
                continue

            group["unfilled_time"] -= new["reading_time"]
            group["chosen_news"].append((new["title"], new["reading_time"]))
            return True

        return False
