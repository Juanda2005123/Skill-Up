from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .basePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class CreateProjectPage(BasePage):
    TITLEFIELD = (By.ID, "id_title")
    REQUIREDPOSITIONFIELD = (By.ID, "id_requiredPosition")
    DESCRIPTIONFIELD = (By.ID, "id_description")
    DAYSDURATIONFIELD = (By.ID, "id_daysDuration")
    BUDGETFIELD = (By.ID, "id_budget")
    CREATEPROJECTBUTTON = (By.ID, "create-project-button")

    EXPERIENCELEVELFIELD = (By.ID, "id_complexity")
    FIELD = (By.XPATH, "/html/body/main/div/div[1]/form/div[4]/div[2]/div/select/option[3]")

    BUDGETERROR = (By.XPATH, "/html/body/div/div/div[2]")

    SKILLS = [
        (By.XPATH, "/html/body/main/div/div[1]/form/div[5]/div/div[2]/input"),
        (By.XPATH, "/html/body/main/div/div[1]/form/div[5]/div/div[8]/input"),
        (By.XPATH, "/html/body/main/div/div[1]/form/div[5]/div/div[7]/input"),
        (By.XPATH, "/html/body/main/div/div[1]/form/div[5]/div/div[6]/input"),
        (By.XPATH, "/html/body/main/div/div[1]/form/div[5]/div/div[31]/input"),
        (By.XPATH, "/html/body/main/div/div[1]/form/div[5]/div/div[32]/input"),
    ]

    def createProject(self, title, requiredPosition, description, budget, days):
        self.enter_text(self.TITLEFIELD, title)
        self.enter_text(self.REQUIREDPOSITIONFIELD, requiredPosition)
        self.enter_text(self.DESCRIPTIONFIELD, description)
        self.enter_text(self.BUDGETFIELD, budget)
        self.enter_text(self.DAYSDURATIONFIELD, days)

        element = self.find_element(self.EXPERIENCELEVELFIELD)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

        self.click(self.FIELD)

        actions = ActionChains(self.driver)
        for skill in self.SKILLS:
            element = self.find_element(skill)
            actions.move_to_element(element).click().perform()

        #selectElement = self.find_elements(by=By.TAG_NAME, value="Option")

        element = self.find_element(self.CREATEPROJECTBUTTON)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def isBudgetError(self):
        element = self.find_element(self.BUDGETERROR)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        return self.find_element(self.BUDGETFIELD).is_displayed()

    def isLastNameShow(self):
        element = self.find_element(self.TITLEFIELD)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        return self.find_element(self.TITLEFIELD).is_displayed()