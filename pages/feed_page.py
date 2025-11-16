from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators


class FeedPage(BasePage):
    def wait_for_counters_to_load(self, time_to_wait=10):
        self.wait_for_element_visibility(FeedPageLocators.TOTAL_ORDERS_COUNTER, time=time_to_wait)

    def get_total_orders_count(self):
        return int(self.find_element(FeedPageLocators.TOTAL_ORDERS_COUNTER).text)

    def get_today_orders_count(self):
        return int(self.find_element(FeedPageLocators.TODAY_ORDERS_COUNTER).text)

    def wait_for_total_orders_to_increase(self, initial_count, time=10):
        def condition(driver):
            current_count = self.get_total_orders_count()
            return current_count > initial_count

        self.wait_for_condition(condition, time=time)

    def wait_for_today_orders_to_increase(self, initial_count, time=10):
        def condition(driver):
            current_count = self.get_today_orders_count()
            return current_count > initial_count

        self.wait_for_condition(condition, time=time)
