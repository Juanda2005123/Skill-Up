from selenium.webdriver.common.by import By
from .basePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains

class DashboardClientPage(BasePage):
    TITLEFIELD = (By.ID, "title-SkillUp")
    MYPROJECTS = (By.ID, "projects-link")
    NOTIFICATION = (By.ID, "notifications-link")
    PROFILE = (By.XPATH, "/html/body/header/div[3]/button")
    VIEWPROFILE = (By.XPATH, "/html/body/header/div[3]/ul/li[1]/a")
    MESSAGES = (By.ID, "messages-link")
    

    def is_search_displayed(self):
        return self.find_element(self.TITLEFIELD).is_displayed()
    
    def navToMyProjects(self):
        self.click(self.MYPROJECTS)

    def navToNotifications(self):
        self.click(self.NOTIFICATION)

    def navToMessages(self):
        self.click(self.MESSAGES)

    def navToProfile(self):
        element = self.find_element(self.PROFILE)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
        
        self.click(self.VIEWPROFILE)

    