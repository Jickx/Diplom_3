from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}"
        )

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}"
        )

    def click_on_element(self, locator):
        self.find_element(locator).click()

    def wait_for_element_to_be_clickable(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_element_visibility(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_invisibility(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(
            EC.invisibility_of_element_located(locator)
        )

    def wait_for_url_to_be(self, url, time=5):
        WebDriverWait(self.driver, time).until(EC.url_to_be(url))

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_condition(self, condition, time=5):
        return WebDriverWait(self.driver, time).until(condition)

    def drag_and_drop(self, source_locator, target_locator):
        element_from = self.find_element(source_locator)
        element_to = self.find_element(target_locator)

        self.driver.execute_script("arguments[0].scrollIntoView(true);", element_from)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element_to)

        actions = ActionChains(self.driver)
        actions.click_and_hold(element_from).pause(0.5).move_to_element(element_to).pause(0.5).release().perform()
