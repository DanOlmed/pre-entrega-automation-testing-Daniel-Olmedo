import pytest
from utils.driver_setup import create_driver
from utils.login import login
from utils.title_check import check_title

@pytest.fixture
def driver():
    drv = create_driver()
    yield drv
    drv.quit()

def test_inventario(driver):
    login(driver)
    check_title(driver, 'Products')
    productos = driver.find_elements("class name", "inventory_item")
    assert len(productos) > 0
    print(f'Se encontraron {len(productos)} productos.')