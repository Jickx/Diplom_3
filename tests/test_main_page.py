from pages.main_page import MainPage


class TestMainPage:

    def test_navigation_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed_button()
        main_page.click_constructor_button()
        main_page.wait_for_assemble_burger_title()
        assert main_page.is_assemble_burger_title_displayed()

    def test_navigation_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.click_order_feed_button()
        main_page.wait_for_feed_url()
        assert "/feed" in driver.current_url

    def test_ingredient_modal_opens(self, driver):
        main_page = MainPage(driver)
        main_page.click_first_ingredient()
        main_page.wait_for_modal_header()
        assert main_page.is_modal_header_displayed()

    def test_ingredient_modal_closes(self, driver):
        main_page = MainPage(driver)
        main_page.click_first_ingredient()
        main_page.wait_for_modal_header()
        main_page.click_modal_close_button()
        main_page.wait_for_modal_to_close()
        assert main_page.is_modal_header_not_present()

    def test_ingredient_counter_increases_on_add(self, driver):
        pass
