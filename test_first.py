def test_first():
    pass


class TestFirst:
    def test_first(self):
        pass

    def test_second(self):
        pass

    def test_third(self):
        pass


def test_second(pytestconfig):
    print(pytestconfig.getoption("shard_num"))
    pass
