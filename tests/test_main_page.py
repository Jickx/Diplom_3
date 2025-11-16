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
        main_page = MainPage(driver)
        ingredient_element = main_page.get_first_filling()
        initial_counter_text = main_page.get_ingredient_counter(ingredient_element)
        initial_count = int(initial_counter_text) if initial_counter_text else 0

        main_page.drag_first_filling_to_constructor()

        expected_count = str(initial_count + 1)
        main_page.wait_for_ingredient_counter_value(main_page.get_first_filling(), expected_count)

        final_counter_text = main_page.get_ingredient_counter(main_page.get_first_filling())
        assert final_counter_text == expected_count
