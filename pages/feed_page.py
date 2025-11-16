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
            return self.get_total_orders_count() > initial_count

        self.wait_for_condition(condition, time=time)

    def wait_for_today_orders_to_increase(self, initial_count, time=10):
        def condition(driver):
            return self.get_today_orders_count() > initial_count

        self.wait_for_condition(condition, time=time)

    def get_in_progress_orders(self):
        elements = self.driver.find_elements(*FeedPageLocators.IN_PROGRESS_ORDERS)
        numbers = []
        for e in elements:
            merged = ''.join(ch for ch in e.text if ch.isdigit()).lstrip('0') or '0'
            if merged:
                numbers.append(merged)
        return numbers

    def wait_for_order_in_progress(self, order_number, time=30):
        order_number = str(order_number).strip()

        def condition(driver):
            elems = driver.find_elements(*FeedPageLocators.IN_PROGRESS_ORDERS)
            for el in elems:
                merged = ''.join(ch for ch in el.text if ch.isdigit()).lstrip('0') or '0'
                if merged == order_number:
                    return True
            return False

        self.wait_for_condition(condition, time=time)
