from django.test import TestCase, Client as TestClient  # Importa TestClient
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from apps.accounts.models import *
from apps.communications.models import *

class TestSecurity(TestCase):
    """
    Clase de pruebas de seguridad para las vistas relacionadas con chats y accesos restringidos.
    Verifica el acceso a las vistas según el rol del usuario y el estado de autenticación.
    """

    def setUp(self):
        """
        Configuración inicial de las pruebas.
        Crea usuarios (cliente y freelancer), perfiles y un chat para realizar las pruebas de acceso.
        """
        self.testClient = TestClient()  # Cliente de prueba para hacer solicitudes HTTP

        # Crear usuarios 'clientUser' y 'freelancerUser' para las pruebas
        self.clientUser = Userk.objects.create_user(username='clientUser', password='testpassword', is_client=True)
        self.freelancerUser = Userk.objects.create_user(username='freelancerUser', password='testpassword', is_freelancer=True)

        # Crear instancias de Client y Freelancer asociadas a los usuarios
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

        # Crear un chat de prueba entre el freelancer y el cliente
        self.chat = Chat.objects.create(
            chatName='testChat',
            freelancer=self.freelancer,
            client=self.testClientInstance
        )

    def testClientAccessToClientMessageHome(self):
        """
        Verifica que un cliente autenticado puede acceder a la vista 'clientMessageHome'.
        """
        self.testClient.login(username='clientUser', password='testpassword')  # Autenticarse como cliente
        response = self.testClient.get(reverse('clientMessageHome'))
        self.assertEqual(response.status_code, 200)

    def testFreelancerAccessToClientMessageHome(self):
        """
        Verifica que un freelancer autenticado no puede acceder a 'clientMessageHome'.
        """
        self.testClient.login(username='freelancerUser', password='testpassword')  # Autenticarse como freelancer
        response = self.testClient.get(reverse('clientMessageHome'))
        self.assertContains(response, 'You are not God to view this page bro')
        self.assertEqual(response.status_code, 200)

    def testUnauthenticatedUserAccessToClientMessageHome(self):
        """
        Verifica que un usuario no autenticado sea redirigido al login al intentar acceder a 'clientMessageHome'.
        """
        response = self.testClient.get(reverse('clientMessageHome'))
        self.assertRedirects(response, '/login/?next=/clientMessageHome/')
        self.assertEqual(response.status_code, 302)

    def testFreelancerAccessToFreelancerMessageHome(self):
        """
        Verifica que un freelancer autenticado puede acceder a 'freelancerMessageHome'.
        """
        self.testClient.login(username='freelancerUser', password='testpassword')  # Autenticarse como freelancer
        response = self.testClient.get(reverse('freelancerMessageHome'))
        self.assertEqual(response.status_code, 200)

    def testClientAccessToFreelancerMessageHome(self):
        """
        Verifica que un cliente autenticado no puede acceder a 'freelancerMessageHome'.
        """
        self.testClient.login(username='clientUser', password='testpassword')  # Autenticarse como cliente
        response = self.testClient.get(reverse('freelancerMessageHome'))
        self.assertContains(response, 'You are not God to view this page bro')
        self.assertEqual(response.status_code, 200)

    def testUnauthenticatedUserAccessToFreelancerMessageHome(self):
        """
        Verifica que un usuario no autenticado sea redirigido al login al intentar acceder a 'freelancerMessageHome'.
        """
        response = self.testClient.get(reverse('freelancerMessageHome'))
        self.assertRedirects(response, '/login/?next=/freelancerMessageHome/')
        self.assertEqual(response.status_code, 302)

    def testAccessToMessageClientViewAsClient(self):
        """
        Verifica que un cliente autenticado puede acceder a un chat específico.
        """
        self.testClient.login(username='clientUser', password='testpassword')  # Autenticarse como cliente
        response = self.testClient.get(reverse('clientMessage', args=[self.chat.chatName]))
        self.assertEqual(response.status_code, 200)

    def testAccessToMessageClientViewAsFreelancer(self):
        """
        Verifica que un freelancer autenticado no puede acceder a un chat del cliente.
        """
        self.testClient.login(username='freelancerUser', password='testpassword')  # Autenticarse como freelancer
        response = self.testClient.get(reverse('clientMessage', args=[self.chat.chatName]))
        self.assertContains(response, 'You are not God to view this page bro')
        self.assertEqual(response.status_code, 200)

    def testAccessToMessageClientViewAsUnauthenticated(self):
        """
        Verifica que un usuario no autenticado sea redirigido al login al intentar acceder a un chat del cliente.
        """
        response = self.testClient.get(reverse('clientMessage', args=[self.chat.chatName]))
        expected_url = f'/login/?next=/clientMessage/{self.chat.chatName}'
        self.assertRedirects(response, expected_url)
        self.assertEqual(response.status_code, 302)

    def testAccessToMessageFreelancerViewAsFreelancer(self):
        """
        Verifica que un freelancer autenticado puede acceder a un chat específico.
        """
        self.testClient.login(username='freelancerUser', password='testpassword')  # Autenticarse como freelancer
        response = self.testClient.get(reverse('freelancerMessage', args=[self.chat.chatName]))
        self.assertEqual(response.status_code, 200)

    def testAccessToMessageFreelancerViewAsUnauthenticated(self):
        """
        Verifica que un usuario no autenticado sea redirigido al login al intentar acceder a un chat del freelancer.
        """
        response = self.testClient.get(reverse('freelancerMessage', args=[self.chat.chatName]))
        expected_url = f'/login/?next=/freelancerMessage/{self.chat.chatName}'
        self.assertRedirects(response, expected_url)
        self.assertEqual(response.status_code, 302)

    def testAccessToClientCreateComprobateChatAsFreelancer(self):
        """
        Verifica que un freelancer autenticado no pueda crear un chat de cliente.
        """
        self.testClient.login(username='freelancerUser', password='testpassword')  # Autenticarse como freelancer
        response = self.testClient.get(reverse('clientCreateComprobateChat', args=[self.clientUser.username]))
        self.assertContains(response, 'You are not God to view this page bro')
        self.assertEqual(response.status_code, 200)

    def testAccessToFreelancerCreateComprobateChatAsClient(self):
        """
        Verifica que un cliente autenticado no pueda crear un chat de freelancer.
        """
        self.testClient.login(username='clientUser', password='testpassword') 
