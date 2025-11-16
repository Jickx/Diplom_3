from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    def set_email(self, email):
        self.wait_for_element_visibility(LoginPageLocators.EMAIL_INPUT)
        self.find_element(LoginPageLocators.EMAIL_INPUT).send_keys(email)

    def set_password(self, password):
        self.wait_for_element_visibility(LoginPageLocators.PASSWORD_INPUT)
        self.find_element(LoginPageLocators.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.wait_for_element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)
        self.js_click(LoginPageLocators.LOGIN_BUTTON)

    def login(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_login_button()
