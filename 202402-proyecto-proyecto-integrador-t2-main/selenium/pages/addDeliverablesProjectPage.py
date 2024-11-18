from selenium.webdriver.common.by import By
from .basePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class AddDeliverablesProjectPage(BasePage):
    MILESTONEFIELD = (By.ID, "id_name")
    ADDMILESTONEBUTTON = (By.ID, "add-milestone-button")

    MODIFY1 = (By.XPATH, "/html/body/main/div/div[1]/div[2]/div[1]/div/a")
    MODIFY2 = (By.XPATH, "/html/body/main/div/div[1]/div[2]/div[2]/div/a")
    MODIFY3 = (By.XPATH, "/html/body/main/div/div[1]/div[2]/div[3]/div/a")

    SENDPROPOSALBUTTON = (By.ID, "send-proposal-button")

    def registerMilestone(self, milestone):
        self.enter_text(self.MILESTONEFIELD, milestone)
        element = self.find_element(self.ADDMILESTONEBUTTON)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def nav1Milestone(self):
        element = self.find_element(self.MODIFY1)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def nav2Milestone(self):
        element = self.find_element(self.MODIFY2)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def nav3Milestone(self):
        element = self.find_element(self.MODIFY3)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def sendProposal(self):
        element = self.find_element(self.SENDPROPOSALBUTTON)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()