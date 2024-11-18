from selenium.webdriver.common.by import By
from .basePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class AddMilestoneDeliverablePage(BasePage):
    NAMEFIELD = (By.ID, "id_name")
    DESCRIPTIONFIELD = (By.ID, "id_description")
    DAYSFIELD = (By.ID, "id_deadlineInDays")

    SAVEBUTTON = (By.ID, "save-button")
    SAVEADDANOTHERBUTTON = (By.ID, "save-add-another-button")
    


    def registerMilestoneSave(self, name, description, days):
        self.enter_text(self.NAMEFIELD, name)
        self.enter_text(self.DESCRIPTIONFIELD, description)
        self.enter_text(self.DAYSFIELD, days)

        element = self.find_element(self.SAVEBUTTON)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def registerMilestoneSaveAddAnother(self, name, description, days):
        self.enter_text(self.NAMEFIELD, name)
        self.enter_text(self.DESCRIPTIONFIELD, description)
        self.enter_text(self.DAYSFIELD, days)

        element = self.find_element(self.SAVEADDANOTHERBUTTON)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

