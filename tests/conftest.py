import random

import pytest


# def pytest_collection_modifyitems(items):
#     random.shuffle(items)
#     for item in items:
#         print(item.path)


@pytest.fixture(scope="session")
def fix_session(request):
    print(f"Session opened")
    yield
    print(f"Session closed")


# @pytest.fixture(params=[1, 2, 3], autouse=True)
# def fix_func(request):
#     print(f"Session {request.param}")
#     yield
#     print(f"Session closed {request.param}")
