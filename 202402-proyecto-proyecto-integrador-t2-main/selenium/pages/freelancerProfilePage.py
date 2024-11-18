from selenium.webdriver.common.by import By
from .basePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains

class FreelancerProfilePage(BasePage):
    APPROVEBUTTON = (By.XPATH, "/html/body/section[1]/div[1]/div/form[1]/button")
    REJECTBUTTON = (By.XPATH, "/html/body/section[1]/div[1]/div/form[2]/button")
    CHATBUTTON = (By.XPATH, "/html/body/section[1]/div[1]/a")


    def approveFreelancer(self):
        self.click(self.APPROVEBUTTON)

    def rejectFreelancer(self):
        self.click(self.REJECTBUTTON)

    def chat(self):
        self.click(self.CHATBUTTON)


