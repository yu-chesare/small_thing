import random


def pytest_collection_modifyitems(items):
    random.shuffle(items)
    for item in items:
        print(item.path)
