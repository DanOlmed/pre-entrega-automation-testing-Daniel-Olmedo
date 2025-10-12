import pytest
from utils.driver_setup import create_driver
from utils.login import login

@pytest.fixture
def driver():
    drv = create_driver()
    yield drv
    drv.quit()

def test_login_url(driver):
    login(driver)
    assert '/inventory.html' in driver.current_url
    print(f'Login OK')

