from selenium.webdriver.common.by import By
from .basePage import BasePage

class InformationProjectPage(BasePage):
    TITLEFIELD = (By.XPATH, "/html/body/main/div/div[1]/h1")
    BROWSEPROJECTS = (By.ID, "find-work-link")
    APPLYBUTTONPROJECT = (By.ID, "button-apply-project")
    CHATBUTTON = (By.ID, "chat-button")

    def is_search_displayed(self):
        return self.find_element(self.TITLEFIELD).is_displayed()
    
    def navToBrowseProjects(self):
        self.click(self.BROWSEPROJECTS)

    def applyProject(self):
        self.click(self.APPLYBUTTONPROJECT)

    def chat(self):
        self.click(self.CHATBUTTON)
    

    