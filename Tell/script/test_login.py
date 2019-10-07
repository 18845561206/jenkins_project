class TestLogin:
    def test_login01(self):
        print("1")
        assert 1
    def test_login02(self):
        print("2")
        assert 0
    def test_login03(self):
        print("3")
        assert 1
# allure generate report/ -o report/html --clean
