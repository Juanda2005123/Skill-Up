from selenium.webdriver.common.by import By
from .basePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains
import time


class ClientMessagePage(BasePage):
    NAMEFIELD = (By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div/div/h5")
    CHATFIELD = (By.ID, "id_body")
    SENDBUTTON = (By.ID, "send-message-button")
    MESSAGE_CONTAINER = (By.ID, "messages")
    MESSAGE_ELEMENTS = (By.CLASS_NAME, "message")

    DROPDOWNMENU = (By.ID, "dropdownMenuButton")
    LOGOUTCLIENT = (By.XPATH, "/html/body/header/div[3]/ul/li[3]/a")

    def isTitleDisplayed(self, name):
        # Encuentra el elemento
        element = self.find_element(self.NAMEFIELD)
        
        # Verifica que el elemento esté visible
        if not element.is_displayed():
            return False
        
        # Verifica que el texto del elemento coincida con el esperado
        return element.text.strip() == name
    
    def sendMessage(self, msg):
        self.enter_text(self.CHATFIELD, msg)
        self.click(self.SENDBUTTON)

    def sendMessageIsDisplayed(self):
        return self.find_element(self.CHATFIELD).is_displayed()
    
    def messageDisplayed(self, msg):
        # Encuentra el contenedor de mensajes
        message_container = self.find_element(self.MESSAGE_CONTAINER)
        
        # Encuentra todos los mensajes dentro del contenedor
        messages = message_container.find_elements(*self.MESSAGE_ELEMENTS)
        
        # Itera sobre los mensajes y verifica si alguno coincide con el texto esperado
        for message in messages:
            if message.text.strip() == msg:
                return True
        
        # Si no se encontró el mensaje, retorna False
        return False
    
    def logOut(self):
        time.sleep(1)

        # Ahora interactúa con el menú desplegable
        dropdown = self.find_element(self.DROPDOWNMENU)
        actions = ActionChains(self.driver)
        actions.move_to_element(dropdown).click().perform()

        # Encuentra y haz clic en el botón de logout
        logout_button = self.find_element(self.LOGOUTCLIENT)
        actions.move_to_element(logout_button).click().perform()