from selenium.webdriver.common.by import By
from .basePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains

class DashboardFreelancerPage(BasePage):
    TITLEFIELD = (By.ID, "title-SkillUp")
    BROWSEPROJECTS = (By.ID, "find-work-link")
    NOTIFICATION = (By.ID, "notifications-link")
    PROFILE = (By.ID, "dropdownMenuButton")
    VIEWPROFILE = (By.XPATH, "/html/body/header/div[3]/ul/li[3]/a")
    MESSAGES = (By.ID, "messages-link")

    def is_search_displayed(self):
        return self.find_element(self.TITLEFIELD).is_displayed()
    
    def navToBrowseProjects(self):
        self.click(self.BROWSEPROJECTS)

    def navToNotifications(self):
        self.click(self.NOTIFICATION)

    def navToProfile(self):
        element = self.find_element(self.PROFILE)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
        
        self.click(self.VIEWPROFILE)

    def navToMessages(self):
        self.click(self.MESSAGES)

    