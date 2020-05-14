from Pages.LoginPages import Login
from Data.TestData import *
import pytest


@pytest.mark.usefixtures("test_setup")
class TestLoginPage():
    def test_fblog(self):
        driver=self.driver
        lg=Login(driver)
        lg.Login1(UserName,Password)
