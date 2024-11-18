from selenium.webdriver.common.by import By
from .basePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class BrowseProjectPage(BasePage):
    FIRSTPROJECT = (By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[1]/div[1]/div/a")
    SECONDPROJECT = (By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/a")
    DROPDOWNMENU = (By.ID, "dropdownMenuButton")
    LOGOUT = (By.XPATH, "/html/body/header/div[3]/ul/li[5]/a")

    def navFirstProject(self):
        self.click(self.FIRSTPROJECT)

    def navSecondProject(self):
        element = self.find_element(self.SECONDPROJECT)
    
        # Usa ActionChains para moverte al elemento
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        
        # Espera 0.5 segundos
        time.sleep(0.5)
        
        # Haz clic en el elemento
        actions.click(element).perform()

    def logOut(self):
        # Espera a que el mensaje desaparezca
        time.sleep(6)

        # Ahora interactúa con el menú desplegable
        dropdown = self.find_element(self.DROPDOWNMENU)
        actions = ActionChains(self.driver)
        actions.move_to_element(dropdown).click().perform()

        # Encuentra y haz clic en el botón de logout
        logout_button = self.find_element(self.LOGOUT)
        actions.move_to_element(logout_button).click().perform()
