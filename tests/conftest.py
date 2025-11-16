import pytest
from selenium import webdriver
from data.urls import Urls
from data.user_data import generate_user_data
from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.fixture(params=["firefox", "chrome"])
def driver(request):
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)
    elif request.param == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options)
        driver.set_window_size(1920, 1080)
    else:
        raise ValueError(f"Browser {request.param} is not supported")

    driver.get(Urls.BASE_URL)

    yield driver

    driver.quit()


@pytest.fixture
def user():
    return generate_user_data()


@pytest.fixture
def logged_in_driver(driver, user):
    driver.get(Urls.LOGIN_URL)
    login_page = LoginPage(driver)
    login_page.login(user["email"], user["password"])

    main_page = MainPage(driver)
    main_page.wait_for_assemble_burger_title()

    return driver
