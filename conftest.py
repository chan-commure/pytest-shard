import pytest


def pytest_collection_modifyitems(session, config, items):
    skip_marker = pytest.mark.skip()

    shard_num = session.config.getoption("shard_num")
    shard_index = session.config.getoption("shard_index")
    print(items)
    for index, item in enumerate(items):
        if shard_num == 1 or index % shard_num != shard_index:
            continue
        items[index].add_marker(skip_marker)


def pytest_addoption(parser):
    parser.addoption("--shard-num", action="store", default=1, type=int)
    parser.addoption("--shard-index", action="store", default=0, type=int)
