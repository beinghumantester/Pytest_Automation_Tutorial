from pages.login_file import LoginPage
from test_data.login_data import url

from utils.data_reader import get_login_data
import pytest

@pytest.mark.parametrize("username,password",get_login_data())
def test_login(driver,username,password):

  
      LoginPage.login(driver, username, password) 

 


     
      







 