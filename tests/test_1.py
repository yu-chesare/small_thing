import pytest

from bookstore.api import Bookstore

@pytest.mark.parametrize("username, password, code",
                         [(None, None, 200),
                          (None, "wrong_pass", 401)])
def test_authorize(username, password, code):
    bookstore = Bookstore()
    assert bookstore.authorize(username, password) == code
