from pages.main_page import MainPage
from pages.feed_page import FeedPage
from data.urls import Urls


class TestOrderFeed:

    def test_total_orders_counter_increases(self, logged_in_driver):
        main_page = MainPage(logged_in_driver)
        feed_page = FeedPage(logged_in_driver)

        # 1. Перейти в ленту заказов и получить начальное значение счетчика
        main_page.click_order_feed_button()
        feed_page.wait_for_url_to_be(Urls.FEED_URL)
        feed_page.wait_for_counters_to_load()
        initial_total_orders = feed_page.get_total_orders_count()

        # 2. Вернуться в конструктор и создать заказ
        main_page.click_constructor_button()
        main_page.wait_for_assemble_burger_title()
        order_number = main_page.create_order_and_get_number()
        assert order_number is not None, "Номер заказа не получен"

        # 3. Снова перейти в ленту заказов и проверить счетчик
        main_page.click_order_feed_button()
        feed_page.wait_for_url_to_be(Urls.FEED_URL)
        feed_page.wait_for_total_orders_to_increase(initial_total_orders)
        final_total_orders = feed_page.get_total_orders_count()

        assert final_total_orders > initial_total_orders, "Счетчик 'Выполнено за всё время' не увеличился"

    def test_today_orders_counter_increases(self, logged_in_driver):
        main_page = MainPage(logged_in_driver)
        feed_page = FeedPage(logged_in_driver)

        # 1. Перейти в ленту заказов и получить начальное значение счетчика заказов на сегодня
        main_page.click_order_feed_button()
        feed_page.wait_for_url_to_be(Urls.FEED_URL)
        feed_page.wait_for_counters_to_load()
        initial_today_orders = feed_page.get_today_orders_count()

        # 2. Вернуться в конструктор и создать заказ
        main_page.click_constructor_button()
        main_page.wait_for_assemble_burger_title()
        order_number = main_page.create_order_and_get_number()
        assert order_number is not None, "Номер заказа не получен"

        # 3. Снова перейти в ленту заказов и проверить счетчик заказов на сегодня
        main_page.click_order_feed_button()
        feed_page.wait_for_url_to_be(Urls.FEED_URL)
        feed_page.wait_for_today_orders_to_increase(initial_today_orders)
        final_today_orders = feed_page.get_today_orders_count()

        assert final_today_orders > initial_today_orders, "Счетчик 'Выполнено сегодня' не увеличился"
