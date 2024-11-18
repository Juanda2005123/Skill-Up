from selenium.webdriver.common.by import By
from .basePage import BasePage

class MessageHomePage(BasePage):
    LATESTCHAT = (By.ID, "latest-chat-button")
    
    def latestChat(self):
        self.click(self.LATESTCHAT)