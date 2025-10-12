import pytest
from utils.driver_setup import create_driver
from utils.login import login

@pytest.fixture
def driver():
    drv = create_driver()
    yield drv
    drv.quit()

def test_carrito(driver):
    login(driver)
    productos = driver.find_elements("class name", "inventory_item")
    productos[0].find_element("tag name", "button").click()
    badge = driver.find_element("class name", "shopping_cart_badge").text
    assert badge == '1'
    print('Carrito OK ->', badge)