from selenium.webdriver.common.by import By
from .basePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class CustomizeProfilePage(BasePage):
    EXPERIENCELEVEL = (By.ID, "id_experience_level")
    EXPERIENCELEVELFIELD = (By.XPATH, "/html/body/div[1]/div[2]/form/div[1]/div/div[2]/select/option[3]")

    DESCRIPTIONFIELD = (By.ID, "id_description")
    LINKEDINFIELD = (By.ID, "id_linkedin_url")
    GITHUBFIELD = (By.ID, "id_github_url")
    INSTAGRAMFIELD = (By.ID, "id_instagram_url")
    SKILLSFIELD = (By.ID, "new_skills")
    BUTTON = (By.ID, "save-changes-button")

    NOTIFICATION = (By.ID, "notifications-link")
    TITLE = (By.XPATH, "/html/body/div[1]/div[2]/form/div[1]/h3")

    def updateFreelancerProfile(self, description, linkedin, github, instragram, skills):
        
        element = self.find_element(self.EXPERIENCELEVEL)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

        self.click(self.EXPERIENCELEVELFIELD)
        
        self.enter_text(self.DESCRIPTIONFIELD, description)
        self.enter_text(self.LINKEDINFIELD, linkedin)
        self.enter_text(self.GITHUBFIELD, github)
        self.enter_text(self.INSTAGRAMFIELD, instragram)
        self.enter_text(self.SKILLSFIELD, skills)

        element = self.find_element(self.BUTTON)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def isDisplayed(self):
        element = self.find_element(self.BUTTON)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()
        return self.find_element(self.TITLE).is_displayed()
        
    
    def navToNotification(self):
        element = self.find_element(self.NOTIFICATION)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()