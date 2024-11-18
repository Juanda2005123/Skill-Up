from selenium.webdriver.common.by import By
from .basePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class ApplyProjectFreelancerPage(BasePage):
    APPROVEBUTTON = (By.ID, "approve-button")
    REJECTBUTTON = (By.ID, "reject-button")

    def approve(self):
        element = self.find_element(self.APPROVEBUTTON)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def reject(self):
        element = self.find_element(self.REJECTBUTTON)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

