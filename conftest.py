import pytest
from selenium import webdriver
from urls import Urls


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Browser {request.param} is not supported")

    driver.get(Urls.BASE_URL)
    driver.maximize_window()

    yield driver

    driver.quit()
