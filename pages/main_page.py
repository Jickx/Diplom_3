from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import Urls


class MainPage(BasePage):

    def click_order_feed_button(self):
        self.click_on_element(MainPageLocators.ORDER_FEED_BUTTON)

    def click_constructor_button(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    def wait_for_assemble_burger_title(self):
        self.wait_for_element_visibility(MainPageLocators.ASSEMBLE_BURGER_TITLE)

    def is_assemble_burger_title_displayed(self):
        return self.find_element(MainPageLocators.ASSEMBLE_BURGER_TITLE).is_displayed()

    def wait_for_feed_url(self):
        self.wait_for_url_to_be(Urls.FEED_URL)

    def click_first_ingredient(self):
        self.click_on_element(MainPageLocators.FIRST_BUN)

    def wait_for_modal_header(self):
        self.wait_for_element_visibility(MainPageLocators.MODAL_HEADER_OPENED)

    def is_modal_header_displayed(self):
        return self.find_element(MainPageLocators.MODAL_HEADER_OPENED).is_displayed()

    def click_modal_close_button(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.click_on_element(MainPageLocators.MODAL_CLOSE_BUTTON)

    def wait_for_modal_to_close(self):
        self.wait_for_element_invisibility(MainPageLocators.MODAL_OPENED)

    def is_modal_header_not_present(self):
        elems = self.driver.find_elements(*MainPageLocators.MODAL_OPENED)
        return len(elems) == 0 or all(not e.is_displayed() for e in elems)

    def get_first_filling(self):
        return self.find_element(MainPageLocators.FIRST_FILLING)

    def get_ingredient_counter(self, ingredient_element):
        counters = ingredient_element.find_elements(*MainPageLocators.INGREDIENT_COUNTER)
        return counters[0].text if counters else None

    def drag_first_filling_to_constructor(self):
        self.drag_and_drop(MainPageLocators.FIRST_FILLING, MainPageLocators.BURGER_CONSTRUCTOR_AREA)

    def wait_for_ingredient_counter_value(self, ingredient_element, value):
        self.wait_for_condition(lambda d: self.get_ingredient_counter(ingredient_element) == value)
