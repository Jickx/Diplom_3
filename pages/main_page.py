from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data.urls import Urls


class MainPage(BasePage):
    """
    Класс главной страницы, содержащий методы для взаимодействия с элементами конструктора и навигации.
    """

    def click_order_feed_button(self):
        """Кликает на кнопку 'Лента заказов'."""
        self.js_click(MainPageLocators.ORDER_FEED_BUTTON)

    def click_constructor_button(self):
        """Кликает на кнопку 'Конструктор'."""
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    def wait_for_assemble_burger_title(self):
        """Ожидает появления заголовка 'Соберите бургер'."""
        self.wait_for_element_visibility(MainPageLocators.ASSEMBLE_BURGER_TITLE)

    def is_assemble_burger_title_displayed(self):
        """Проверяет, отображается ли заголовок 'Соберите бургер'."""
        return self.find_element(MainPageLocators.ASSEMBLE_BURGER_TITLE).is_displayed()

    def wait_for_feed_url(self):
        """Ожидает, пока URL не станет URL'ом ленты заказов."""
        self.wait_for_url_to_be(Urls.FEED_URL)

    def click_first_ingredient(self):
        """Кликает на первый ингредиент (булку)."""
        self.click_on_element(MainPageLocators.FIRST_BUN)

    def wait_for_modal_header(self):
        """Ожидает появления заголовка в модальном окне ингредиента."""
        self.wait_for_element_visibility(MainPageLocators.MODAL_HEADER_OPENED)

    def is_modal_header_displayed(self):
        """Проверяет, отображается ли заголовок в модальном окне."""
        return self.find_element(MainPageLocators.MODAL_HEADER_OPENED).is_displayed()

    def click_modal_close_button(self):
        """Кликает на кнопку закрытия модального окна."""
        self.wait_for_element_to_be_clickable(MainPageLocators.MODAL_CLOSE_BUTTON)
        self.js_click(MainPageLocators.MODAL_CLOSE_BUTTON)

    def wait_for_modal_to_close(self):
        """Ожидает, пока модальное окно не закроется."""
        self.wait_for_element_invisibility(MainPageLocators.MODAL_OPENED)

    def is_modal_header_not_present(self):
        """Проверяет, отсутствует ли модальное окно на странице."""
        elems = self.driver.find_elements(*MainPageLocators.MODAL_OPENED)
        return len(elems) == 0 or all(not e.is_displayed() for e in elems)

    def click_place_order_button(self):
        """Кликает на кнопку 'Оформить заказ'."""
        self.click_on_element(MainPageLocators.PLACE_ORDER_BUTTON)

    def wait_for_order_modal(self):
        """Ожидает появления модального окна с подтверждением заказа."""
        self.wait_for_element_visibility(MainPageLocators.ORDER_MODAL_OPENED)

    def get_order_number(self):
        """Получает номер заказа, дождавшись его появления."""
        self.wait_for_condition(
            lambda driver: self.find_element(MainPageLocators.ORDER_NUMBER).text != "9999",
            time=20
        )
        return self.find_element(MainPageLocators.ORDER_NUMBER).text

    def get_first_filling(self):
        """Возвращает веб-элемент первой начинки."""
        return self.find_element(MainPageLocators.FIRST_FILLING)

    def get_ingredient_counter(self, ingredient_element):
        """Получает значение счетчика для указанного ингредиента."""
        counters = ingredient_element.find_elements(*MainPageLocators.INGREDIENT_COUNTER)
        return counters[0].text if counters else None

    def drag_first_filling_to_constructor(self):
        """Перетаскивает первую начинку в конструктор."""
        self.drag_and_drop(MainPageLocators.FIRST_FILLING, MainPageLocators.BURGER_CONSTRUCTOR_AREA)

    def drag_first_bun_to_constructor(self):
        """Перетаскивает первую булку в конструктор."""
        self.drag_and_drop(MainPageLocators.FIRST_BUN, MainPageLocators.BURGER_CONSTRUCTOR_AREA)

    def create_order_and_get_number(self):
        """
        Создает заказ (добавляет булку и начинку) и возвращает его номер.
        """
        self.drag_first_bun_to_constructor()
        self.drag_first_filling_to_constructor()
        self.click_place_order_button()
        self.wait_for_order_modal()
        order_number = self.get_order_number()
        self.click_modal_close_button()
        self.wait_for_modal_to_close()
        return order_number

    def wait_for_ingredient_counter_value(self, ingredient_element, value):
        """Ожидает, пока счетчик ингредиента не примет указанное значение."""
        self.wait_for_condition(lambda d: self.get_ingredient_counter(ingredient_element) == value)
