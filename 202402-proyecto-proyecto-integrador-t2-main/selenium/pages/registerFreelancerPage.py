from selenium.webdriver.common.by import By
from .basePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class RegisterFreelancerPage(BasePage):
    FIRSTNAMEFIELD = (By.ID, "id_first_name")
    LASTNAMEFIELD = (By.ID, "id_last_name")
    USERNAMEFIELD = (By.ID, "id_username")
    EMAILFIELD = (By.ID, "id_email")
    PASSWORD1FIELD = (By.ID, "id_password1")
    PASSWORD2FIELD = (By.ID, "id_password2")
    IDENTIFICATIONFIELD = (By.ID, "id_identification")
    PHONENUMBERFIELD = (By.ID, "id_phoneNumber")
   
    ERROR = (By.XPATH, "/html/body/div/div/div/main/form/div[8]")

    # Botón de envío
    SUBMITBUTTON = (By.CSS_SELECTOR, ".btn-submit")

    LANDPAGEBUTTON = (By.ID, "landpage-skillUp")
    

    def register(self, first_name, last_name, username, email, password1, password2, phone_number, identification):
        # Ingresar los valores en los campos correspondientes
        self.enter_text(self.FIRSTNAMEFIELD, first_name)
        self.enter_text(self.LASTNAMEFIELD, last_name)
        self.enter_text(self.USERNAMEFIELD, username)
        self.enter_text(self.EMAILFIELD, email)
        self.enter_text(self.PASSWORD1FIELD, password1)
        self.enter_text(self.PASSWORD2FIELD, password2)
        self.enter_text(self.IDENTIFICATIONFIELD, identification)
        self.enter_text(self.PHONENUMBERFIELD, phone_number)

        # Hacer clic en el botón de envío
        element = self.find_element(self.SUBMITBUTTON)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()


    def errorMessageDisplayed(self):
        return self.find_element(self.ERROR).is_displayed()
    
    
    def landpageRedirect(self):
        element = self.find_element(self.LANDPAGEBUTTON)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def errorEmptyField(self):
        return self.find_element(self.LASTNAMEFIELD).is_displayed()