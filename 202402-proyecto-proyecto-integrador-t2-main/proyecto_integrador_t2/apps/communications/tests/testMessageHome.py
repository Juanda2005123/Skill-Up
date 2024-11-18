from django.test import TestCase, Client as TestClient  # Importa TestClient
from django.urls import reverse
from django.contrib.auth import get_user_model
from apps.accounts.models import *
from apps.communications.models import Chat

class TestMessageHome(TestCase):
    """
    Clase para pruebas de las vistas de inicio de mensajes para clientes y freelancers.
    """

    def setUp(self):
        """
        Configuración inicial para las pruebas:
        - Creación de usuarios cliente y freelancer.
        - Creación de perfiles asociados (Client y Freelancer).
        - Creación de un chat inicial entre cliente y freelancer.
        """
        self.testClient = TestClient()

        # Crear usuarios cliente y freelancer
        self.clientUser = Userk.objects.create_user(username='clientUser', password='testpassword', is_client=True)
        self.freelancerUser = Userk.objects.create_user(username='freelancerUser', password='testpassword', is_freelancer=True)
        
        # Instancias de Client y Freelancer
        self.country = Country.objects.get(code="CO")  # Colombia
        self.city = City.objects.get(name="Bogotá", country=self.country)  # Ciudad en Colombia
        
        # Instancias de Client y Freelancer
        self.testClientInstance = Client.objects.create(
            user=self.clientUser,
            phoneNumber=123456789,
            taxId=1234567890,
            companyName='TestCompany',
            typeOfCompany='Software',
            businessVertical='IT',
            country=self.country,
            city=self.city,
            address='Av. El Dorado',
        )
        
        self.freelancer = Freelancer.objects.create(
            user=self.freelancerUser,
            phoneNumber='987654321',
            identification='0987654321',
            email='freelancer@example.com',
        )
        
        # Crear un chat inicial entre cliente y freelancer
        self.chat = Chat.objects.create(
            chatName='testChat',
            freelancer=self.freelancer,
            client=self.testClientInstance
        )

    def test_client_message_home_view(self):
        """
        Prueba que el cliente pueda ver la lista de chats y que el chat más reciente
        se muestre en primer lugar.
        """
        # Iniciar sesión como cliente
        self.testClient.login(username='clientUser', password='testpassword')

        # Acceder a la vista de clientMessageHome
        response = self.testClient.get(reverse('clientMessageHome'))

        # Verificar que la respuesta tiene el código HTTP 200
        self.assertEqual(response.status_code, 200)

        # Verificar que los contextos de chats y el último chat están presentes
        self.assertIn('chats', response.context)
        self.assertIn('latestChat', response.context)

        # Verificar que el último chat sea el chat creado en la configuración inicial
        self.assertEqual(response.context['latestChat'], self.chat)

    def test_freelancer_message_home_view(self):
        """
        Prueba que el freelancer pueda ver la lista de chats y que el chat más reciente
        se muestre en primer lugar.
        """
        # Iniciar sesión como freelancer
        self.testClient.login(username='freelancerUser', password='testpassword')

        # Acceder a la vista de freelancerMessageHome
        response = self.testClient.get(reverse('freelancerMessageHome'))

        # Verificar que la respuesta tiene el código HTTP 200
        self.assertEqual(response.status_code, 200)

        # Verificar que los contextos de chats y el último chat están presentes
        self.assertIn('chats', response.context)
        self.assertIn('latestChat', response.context)

        # Verificar que el último chat sea el chat creado en la configuración inicial
        self.assertEqual(response.context['latestChat'], self.chat)
