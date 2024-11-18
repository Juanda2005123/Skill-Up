from django.test import TestCase
from django.test import Client as TestClient
from django.urls import reverse
from apps.accounts.models import *

class TestLandPage(TestCase):
    """
    Clase de pruebas unitarias para verificar la funcionalidad de la página de inicio (landpage).
    """

    def setUp(self):
        """
        Configuración inicial para las pruebas de la landpage.
        Se define el cliente de prueba y la URL de la landpage.
        """
        self.client = TestClient()
        self.landpage = reverse('landpage')

    def test_LandpageStatusCode(self):
        """
        Test para verificar que la landpage carga correctamente con un código de estado HTTP 200.
        Comprueba que la página se renderiza sin errores.
        """
        response = self.client.get(self.landpage)
        # Verifica que el código de estado HTTP sea 200
        self.assertEqual(response.status_code, 200)

    def test_LandpageContainsTitle(self):
        """
        Test para verificar que el título 'SkillUp' esté presente en la landpage.
        Este test busca una etiqueta específica en el contenido HTML.
        """
        response = self.client.get(self.landpage)
        # Verifica que 'SkillUp' esté en el contenido HTML de la respuesta
        self.assertContains(response, '<h1 class="u-text u-text-default u-text-1">SkillUp</h1>')

    def test_LandpageContainsNavigationLinks(self):
        """
        Test para verificar que los enlaces de navegación principales ('Find Work', 'Find Talent', 'Log In') están presentes en la página.
        Esto asegura que los usuarios puedan acceder a las principales funcionalidades desde la landpage.
        """
        response = self.client.get(self.landpage)
        # Verifica que el enlace 'Find Work' esté en el HTML
        self.assertContains(response, 'Find Work')
        # Verifica que el enlace 'Find Talent' esté en el HTML
        self.assertContains(response, 'Find Talent')
        # Verifica que el enlace 'Log In' esté en el HTML
        self.assertContains(response, 'Log In')
