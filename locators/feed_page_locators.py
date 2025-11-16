from selenium.webdriver.common.by import By


class FeedPageLocators:
    TOTAL_ORDERS_COUNTER = (
        By.XPATH,
        ".//div[p[text()='Выполнено за все время:']]/p[contains(@class, 'OrderFeed_number__2MbrQ')]"
    )
    TODAY_ORDERS_COUNTER = (
        By.XPATH,
        ".//div[p[text()='Выполнено за сегодня:']]/p[contains(@class, 'OrderFeed_number__2MbrQ')]"
    )
