from selenium.webdriver.common.by import By
from .basePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class NotificationPage(BasePage):
    FIRST_NOTIFICATION = (By.XPATH, "/html/body/div/div/div[1]")
    FIRST_NOTIFICATION_TEXT = (By.XPATH, "/html/body/div/div/div[1]//p")  # XPath para el texto dentro del <p>
    DROPDOWNMENU = (By.ID, "dropdownMenuButton")
    LOGOUTCLIENT = (By.XPATH, "/html/body/header/div[3]/ul/li[3]/a")
    LOGOUTFREELANCER = (By.XPATH, "/html/body/header/div[3]/ul/li[5]/a")
    READ = (By.XPATH, "/html/body/div/ul/li[2]/a")
    DELIVERWORK = (By.ID, "deliver-work-link")

    def clickNotificationLink(self):
        """
        Encuentra y hace clic en el enlace dentro de la primera notificación.
        """
        try:
            # Encuentra la primera notificación
            notification = self.find_element(self.FIRST_NOTIFICATION)

            # Encuentra el enlace dentro de la notificación
            notification_link = notification.find_element(By.XPATH, ".//a")

            # Haz clic en el enlace
            notification_link.click()
        except Exception as e:
            print(f"Error al intentar hacer clic en el enlace de la notificación: {e}")
            raise

    def logOutClient(self):
        time.sleep(6)

        # Ahora interactúa con el menú desplegable
        dropdown = self.find_element(self.DROPDOWNMENU)
        actions = ActionChains(self.driver)
        actions.move_to_element(dropdown).click().perform()

        # Encuentra y haz clic en el botón de logout
        logout_button = self.find_element(self.LOGOUTCLIENT)
        actions.move_to_element(logout_button).click().perform()

    def logOutFreelancer(self):
        time.sleep(6)

        # Ahora interactúa con el menú desplegable
        dropdown = self.find_element(self.DROPDOWNMENU)
        actions = ActionChains(self.driver)
        actions.move_to_element(dropdown).click().perform()

        # Encuentra y haz clic en el botón de logout
        logout_button = self.find_element(self.LOGOUTFREELANCER)
        actions.move_to_element(logout_button).click().perform()

    def isNotificationDisplayed(self, expectedText):
        """
        Verifica que:
        1. La primera notificación esté visible.
        2. El texto del <p> coincida con el texto esperado.

        :param expected_text: Texto esperado dentro del <p>.
        :return: True si ambas condiciones son verdaderas, False en caso contrario.
        """
        try:
            # Verificar que la notificación esté visible
            notification = self.find_element(self.FIRST_NOTIFICATION)
            if not notification.is_displayed():
                return False
            
            # Extraer y comparar el texto del <p>
            notification_text_element = self.find_element(self.FIRST_NOTIFICATION_TEXT)
            actual_text = notification_text_element.text.strip()  # Obtener y limpiar el texto
            return actual_text == expectedText
        except Exception as e:
            # Si ocurre un error (por ejemplo, elemento no encontrado), regresar False
            return False
        
    def readed(self):
        self.click(self.READ)

    def deliverWork(self):
        self.click(self.DELIVERWORK)
