from unittest.mock import Mock, patch

import pytest

from tech_news.analyzer.reading_plan import ReadingPlanService


@pytest.fixture
def reading_plan_service():
    return ReadingPlanService()


@pytest.fixture
def news_mock():
    return [
        {
            "url": "https://blog.betrybe.com/novidades/noticia-bacana",
            "title": "Notícia 1",
            "timestamp": "04/04/2021",
            "writer": "w2k",
            "reading_time": 4,
            "summary": "Python vai dominar o mundo",
            "category": "Noticias",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia-bacana",
            "title": "Notícia 2",
            "timestamp": "04/04/2021",
            "writer": "w2k",
            "reading_time": 5,
            "summary": "Python vai dominar o mundo",
            "category": "Tecnologia",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia-bacana",
            "title": "Notícia 3",
            "timestamp": "04/04/2021",
            "writer": "w2k",
            "reading_time": 15,
            "summary": "Python vai dominar o mundo",
            "category": "Ferramentas",
        },
        {
            "url": "https://blog.betrybe.com/novidades/noticia-bacana",
            "title": "Notícia 4",
            "timestamp": "04/04/2021",
            "writer": "w2k",
            "reading_time": 20,
            "summary": "Python vai dominar o mundo",
            "category": "Ferramentas",
        },
    ]


def test_reading_plan_group_news(reading_plan_service, news_mock):
    with pytest.raises(
        ValueError,
        match="Valor 'available_time' deve ser maior que zero",
    ):
        reading_plan_service.group_news_for_available_time(0)

    mock_find_news = Mock(return_value=news_mock)
    with patch("tech_news.analyzer.reading_plan.find_news", mock_find_news):
        result = reading_plan_service.group_news_for_available_time(10)

    expected_readable = [
        {
            'chosen_news': [('Notícia 1', 4), ('Notícia 2', 5)],
            'unfilled_time': 1,
        }
    ]

    expected_unreadable = [('Notícia 3', 15), ('Notícia 4', 20)]

    assert len(result['readable']) == 1
    assert result['readable'][0] == expected_readable[0]
    assert len(result['unreadable']) == 2
    assert result['unreadable'] == expected_unreadable
