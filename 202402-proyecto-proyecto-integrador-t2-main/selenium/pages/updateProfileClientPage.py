from selenium.webdriver.common.by import By
from .basePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class UpdateProfileClientPage(BasePage):
    DESCRIPTIONCOMPANYFIELD = (By.ID, "id_description_company")
    DESCRIPTIONCOMPANYLABEL = (By.XPATH, "/html/body/div/div[2]/form/div[1]/div/div[2]/label")
    NOTIFICATION = (By.ID, "notifications-link")
    BUTTON = (By.XPATH, "/html/body/div/div[2]/form/button")


    def updateCompanyDescription(self, descriptionCompany):
        self.enter_text(self.DESCRIPTIONCOMPANYFIELD, descriptionCompany)

        element = self.find_element(self.BUTTON)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def isDisplayed(self):
        return self.find_element(self.DESCRIPTIONCOMPANYLABEL).is_displayed()
    
    def navToNotification(self):
        element = self.find_element(self.NOTIFICATION)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()