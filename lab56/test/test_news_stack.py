import pytest
from news_stack import NewsStack

def test_eject():
    news_stack = NewsStack()
    news_stack.news = ['first message']

    res = news_stack.eject()

    assert res == 'first message'
    assert len(news_stack.news) == 0

def test_add_last_message():
    news_stack = NewsStack()
    news_stack.last_message = 'last message'

    news_stack.add_last_message()

    assert len(news_stack.news) == 1
