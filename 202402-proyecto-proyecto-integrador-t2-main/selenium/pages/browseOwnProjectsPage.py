from selenium.webdriver.common.by import By
from .basePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BrowseOwnProjectsPage(BasePage):

    PROJECT_CARDS = (By.CLASS_NAME, "project-card")
    PROJECT_TITLE = ".//h4"
    APPROVEBUTTON = (By.ID, "approve-button")
    REJECTBUTTON = (By.ID, "reject-button")

    def isTitleDisplayed(self, title):
        # Encuentra todas las tarjetas de proyecto
        project_cards = self.find_elements(self.PROJECT_CARDS)
        
        # Busca la tarjeta que contiene el título dado
        for card in project_cards:
            title_element = card.find_element(By.XPATH, self.PROJECT_TITLE)
            if title_element.text.strip() == title:
                return True  # Retorna el contenedor del proyecto correspondiente
        
        raise Exception(f"Project with title '{title}' not found.")

    def approve(self):
        element = self.find_element(self.APPROVEBUTTON)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def reject(self):
        element = self.find_element(self.REJECTBUTTON)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

