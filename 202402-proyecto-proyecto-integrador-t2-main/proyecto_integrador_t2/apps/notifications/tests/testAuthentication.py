from django.test import TestCase, Client as TestClient  # Importa TestClient
from django.urls import reverse
from django.contrib.auth import get_user_model
from apps.accounts.models import *
from apps.notifications.models import *

class TestSecurity(TestCase):
    """
    Pruebas de seguridad para garantizar el acceso adecuado a las notificaciones
    según el rol del usuario (cliente o freelancer).
    """

    def setUp(self):
        """
        Configura los datos necesarios para las pruebas.
        Crea un cliente y un freelancer con sus perfiles asociados.
        """
        self.testClient = TestClient()  # Cliente de pruebas HTTP
        # Crear usuarios 'clientUser' y 'freelancerUser'
        self.clientUser = Userk.objects.create_user(username='clientUser', password='testpassword', is_client=True)
        self.freelancerUser = Userk.objects.create_user(username='freelancerUser', password='testpassword', is_freelancer=True)

        # Crear instancias de Client y Freelancer asociadas a los usuarios
        self.testClientInstance = Client.objects.create(
            user=self.clientUser,
            phoneNumber='123456789',
            taxId='1234567890',
            companyName='TestCompany',
            typeOfCompany='Software',
            businessVertical='IT',
            countryOfLocation='Colombia',
            city='Bogotá',
            address='Av. El Dorado',
        )
        
        self.freelancer = Freelancer.objects.create(
            user=self.freelancerUser,
            phoneNumber='987654321',
            identification='0987654321',
            email='freelancer@example.com',
        )

    def testClientAccessToNotifications(self):
        """
        Verifica que un cliente autenticado puede acceder a las notificaciones.
        """
        self.testClient.login(username='clientUser', password='testpassword')  # Iniciar sesión como cliente

        # Acceder a la vista de notificaciones
        response = self.testClient.get(reverse('notifications'))

        # Verificar que el acceso está permitido (código de respuesta 200)
        self.assertEqual(response.status_code, 200)

    def testFreelancerAccessToNotifications(self):
        """
        Verifica que un freelancer autenticado puede acceder a las notificaciones.
        """
        self.testClient.login(username='freelancerUser', password='testpassword')  # Iniciar sesión como freelancer

        # Acceder a la vista de notificaciones
        response = self.testClient.get(reverse('notifications'))

        # Verificar que el acceso está permitido (código de respuesta 200)
        self.assertEqual(response.status_code, 200)
