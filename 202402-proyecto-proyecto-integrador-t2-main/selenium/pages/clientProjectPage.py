from selenium.webdriver.common.by import By
from .basePage import BasePage

class ClientProjectPage(BasePage):
    CREATEPROJECTBUTTON = (By.ID, "create-project")
    PROJECTS_LIST = (By.CLASS_NAME, "project-list")

    PROJECT_CARDS = (By.CLASS_NAME, "project-card")
    PROJECT_TITLE = ".//h4"  # Título del proyecto relativo al contenedor de la tarjeta
    EDIT_BUTTON = ".//a[contains(@class, 'btn-outline-primary')]"
    PROJECT_TITLES = (By.CSS_SELECTOR, ".project-card h4")


    def createProject(self):
        self.click(self.CREATEPROJECTBUTTON)

    def findProjectCardByTitle(self, title):
        # Encuentra todas las tarjetas de proyecto
        project_cards = self.find_elements(self.PROJECT_CARDS)
        
        # Busca la tarjeta que contiene el título dado
        for card in project_cards:
            title_element = card.find_element(By.XPATH, self.PROJECT_TITLE)
            if title_element.text.strip() == title:
                return card  # Retorna el contenedor del proyecto correspondiente
        
        raise Exception(f"Project with title '{title}' not found.")

    def updateProject(self, title):
        # Encuentra el contenedor de la tarjeta del proyecto
        project_card = self.findProjectCardByTitle(title)
        
        # Encuentra el botón "Editar" dentro de este contenedor
        edit_button = project_card.find_element(By.XPATH, self.EDIT_BUTTON)
        edit_button.click()

    def projectDisplayed(self, title):

        project_titles = self.find_elements(self.PROJECT_TITLES)
        
        # Verificar si el título específico está en la lista de proyectos
        for project in project_titles:
            if title in project.text:
                return True  # Si el título se encuentra, se ha creado el proyecto

        return False