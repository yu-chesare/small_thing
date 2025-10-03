import sys

import pytest

from bookstore.api import Bookstore


class Tests_book:
    @pytest.fixture(scope="class", autouse=True)
    def bookstore(self):
        return Bookstore()

    @pytest.mark.parametrize(
        "username, password, code", [(None, None, 200), (None, "wrong_pass", 401)]
    )
    def test_authorize(self, bookstore, username, password, code):
        assert bookstore.authorize(username, password) == code

    @pytest.mark.xfail
    def test_put(self, bookstore):
        response = bookstore.put_book()
        print(response)
        assert response.status_code == 200

    @pytest.mark.skipif(condition="venv/bin/pytest" in sys.argv[0], reason="Do not run this test from console")
    def test_to_skip(self):
        print(sys.argv)
        pass