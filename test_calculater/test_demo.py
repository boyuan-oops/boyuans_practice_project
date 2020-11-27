def setup_module():
    print("setup module")


def teardown_module():
    print("teardown module")


def setup_function():
    print("function setup")


def test_fun1():
    print("func1")


class TestDemo:
    def setup_class(self):
        print("类setup")

    def teardown_class(self):
        print("类teardown")

    def setup(self):
        print("方法setup")

    def test_demo1(self):
        print("demo1")

    def teardown(self):
        print("方法teardown")
